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

	def get_offers_available(self):
		return Offer.objects.filter(subcategory__category=self, options__start_time__lte=datetime.today(), options__end_time__gte=datetime.today()).order_by('-date_created')

	class Meta:
		verbose_name = u'Categoria'
		verbose_name_plural = u'Categorias'


class SubCategory(models.Model):
	name = models.CharField(u'Nome', max_length=255)
	category = models.ForeignKey(Category, related_name="subcategories")

	def __unicode__(self):
		return '%s - %s' % (self.name, self.category.name)

	class Meta:
		verbose_name = u'SubCategoria'
		verbose_name_plural = u'SubCategorias'

class Interest(models.Model):
	name = models.CharField(u'Nome', max_length=255)
	category = models.ForeignKey(Category, related_name='interests')

	def __unicode__(self):
		return '%s - %s' % (self.name, self.category.name)

	class Meta:
		verbose_name = u'Interesse'
		verbose_name_plural = u'Interesses'


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
	subcategory = models.ForeignKey(SubCategory, verbose_name=u'Sub Categoria')
	interests = models.ManyToManyField(Interest, verbose_name=u'Interesses')
	highlight = models.BooleanField(u'Destaque', default=False)
	highlight_image = models.ImageField(verbose_name=u'Imagem Destaque', upload_to='oferta/')
	affiliate = models.ForeignKey(Affiliate, verbose_name=u'Franqueado', blank=True, null=True)
	bought = models.IntegerField(u'Comprados', default=0)
	bought_virtual = models.IntegerField(u'Quantidade virtual')
	max_by_user = models.IntegerField(u'Máximo por pessoa', blank=True, null=True)
	percent_by_site = models.DecimalField(u'Percentual do site', decimal_places=2, max_digits=10)
	percent_cashback = models.DecimalField(u'Percentual de CashBack', decimal_places=2, max_digits=10)
	city = models.ForeignKey(City, verbose_name=u'Cidade')
	description = tinymce_models.HTMLField(verbose_name=u'Descrição')
	when_to_use = tinymce_models.HTMLField()
	how_to_use = tinymce_models.HTMLField()
	good_to_know = tinymce_models.HTMLField()
	date_created = models.DateTimeField(auto_now_add=True)

	objects = OfferManager()

	class Meta:
		verbose_name = u'Oferta'
		verbose_name_plural = u'Ofertas'

	def __unicode__(self):
		return self.title

	@property
	def partner(self):
		return self.options.all()[0].filial.partner.name

	def bought_total(self):
		return self.bought + self.bought_virtual

	def first_option(self):
		return self.options.filter(start_time__lte=datetime.today(), end_time__gte=datetime.today()).order_by('new_price')[0]

	def other_options(self):
		return self.options.all().exlude(id=self.first_option().id)

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

	def discount(self):
		return 100 * self.new_price / self.old_price

	def time_remaining(self):
		date = self.end_time - timezone.now()
		# return datetime.strptime(date, "%a %b %d %H:%M:%S %Z %Y")
		return "%sd %.2d:%.2d:%.2d" % (date.days,date.seconds//3600,(date.seconds//60)%60, date.seconds%60)

