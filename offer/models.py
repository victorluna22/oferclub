# coding: utf-8
from datetime import datetime
from django.utils import timezone
from django.db import models
from offer.slugify import unique_slugify as slugify
from tinymce import models as tinymce_models
from account.models import City, Filial, Affiliate

DE_POR = 1
APARTIR_DE = 2

TYPES = (
	(DE_POR, "DE/POR"),
	(APARTIR_DE, "A PARTIR DE"),
	)

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Categoria'
		verbose_name_plural = u'Categorias'

class OfferManager(models.Manager):
	def latest_offers(self, format='json', limit=8):
		offers = self.all().order_by('-date_created')[:limit]
		return self.prepare_dict(offers)

	def bestsellers(self, format='json', limit=8):
		offers = self.all().order_by('-bought')[:limit]
		return self.prepare_dict(offers)

	def prepare_dict(self, offers):
		data = []
		for offer in offers:
			option = offer.options.all()[0]
			fields = {}
			fields["title"] = str(offer.title)
			fields["partner"] = str(option.filial.partner.name)
			fields["city"] = str(offer.city.name)
			if offer.options.all().count() == 1:
				fields["old_price"] = float(option.old_price)
			fields["new_price"] = float(option.new_price)
			fields["cashback"] = float(offer.percent_cashback)
			fields["quantity"] = int(offer.bought + offer.bought_virtual)
			data.append(fields)
		return data

class Offer(models.Model):
	title = models.CharField(u'Título', max_length=255)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	category = models.ForeignKey(Category, verbose_name=u'Categoria')
	highlight = models.BooleanField(u'Destaque', default=False)
	highlight_image = models.ImageField(verbose_name=u'Imagem Destaque', upload_to='oferta/')
	affiliate = models.ForeignKey(Affiliate, verbose_name=u'Franqueado', blank=True, null=True)
	bought = models.IntegerField(u'Comprados', default=0)
	bought_virtual = models.IntegerField(u'Quantidade virtual')
	max_by_user = models.IntegerField(u'Máximo por pessoa', blank=True, null=True)
	percent_by_site = models.DecimalField(u'Percentual do site', decimal_places=2, max_digits=10)
	percent_cashback = models.DecimalField(u'Percentual de CashBack', decimal_places=2, max_digits=10)
	city = models.ForeignKey(City, verbose_name=u'Cidade')
	description = tinymce_models.HTMLField()
	regulation = tinymce_models.HTMLField()
	date_created = models.DateTimeField(auto_now_add=True)

	objects = OfferManager()

	class Meta:
		verbose_name = u'Oferta'
		verbose_name_plural = u'Ofertas'

	def __unicode__(self):
		return self.title

	@property
	def partner(self):
		return self.options.all()[0]

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(instance=self, value=self.title, slug_separator='-')
		return super(Offer, self).save(*args, **kwargs)


class Image(models.Model):
	name = models.ImageField(verbose_name=u'Imagem', upload_to='oferta/')
	offer = models.ForeignKey(Offer, related_name='images')

	class Meta:
		verbose_name = u'Imagem'
		verbose_name_plural = u'Imagens'

	def __unicode__(self):
		return self.name.name

class Option(models.Model):
	offer = models.ForeignKey(Offer, related_name='options')
	filial = models.ForeignKey(Filial, related_name='offers')
	title = models.CharField(u'Título', max_length=255)
	old_price = models.DecimalField(u'Preço sem desconto', decimal_places=2, max_digits=10, blank=True, null=True)
	new_price = models.DecimalField(u'Preço com desconto', decimal_places=2, max_digits=10)
	quantity = models.IntegerField(u'Quantidade')
	start_time = models.DateTimeField(u'Começa em')
	end_time = models.DateTimeField(u'Termina em')
	date_expiration = models.DateField(u'Expira em')
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = u'Opção'
		verbose_name_plural = u'Opções'

	def __unicode__(self):
		return self.title

	def is_available(self):
		# import pdb;pdb.set_trace()
		today = timezone.now()
		if today >= self.start_time and today < self.end_time:
			return True
		return False
