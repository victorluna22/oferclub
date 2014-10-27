# coding: utf-8
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Count
from django.core.urlresolvers import reverse_lazy
from offer.slugify import unique_slugify as slugify
from tinymce import models as tinymce_models
from account.models import City, Filial, Affiliate

DE_POR = 1
APARTIR_DE = 2

TYPES = (
	(DE_POR, "DE/POR"),
	(APARTIR_DE, "A PARTIR DE"),
	)

class Type(models.Model):
	name = models.CharField(u'Nome', max_length=255)
	slug = models.SlugField(max_length=255, unique=True, blank=True)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	type = models.ForeignKey(Type, related_name='categories')

	def __unicode__(self):
		return self.name

	def get_offers_available(self, id_city):
		return Offer.objects.filter(subcategory__category=self, options__start_time__lte=datetime.today(), options__end_time__gte=datetime.today(), city__id=id_city).order_by('-date_created').distinct()

	class Meta:
		verbose_name = u'Categoria'
		verbose_name_plural = u'Categorias'


class SubCategory(models.Model):
	name = models.CharField(u'Nome', max_length=255)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
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
	def latest_offers(self, id_type, id_city, format='json', limit=8):
		offers = self.select_related('city').filter(subcategory__category__type__id=id_type, city__id=id_city).order_by('-date_created')[:limit]
		return self.prepare_dict(offers)

	def bestsellers(self, id_type, id_city, format='json', limit=8):
		offers = self.select_related('city').filter(subcategory__category__type__id=id_type, city__id=id_city).order_by('-bought')[:limit]
		return self.prepare_dict(offers)

	def prepare_dict(self, offers):
		data = []
		for offer in offers:
			option = offer.first_option()
			fields = {}
			fields["title"] = str(offer.title)
			fields["partner"] = str(option.filial.partner.name)
			fields["link"] = reverse_lazy('offer:offer_detail', kwargs={"slug": offer.slug}).__str__()
			fields["imagem"] = "/media/" + str(offer.image_grid)
			fields["city"] = str(offer.city.name)
			if offer.options.all().count() == 1:
				fields["before_price"] = float(option.old_price)
			else:
				fields["before_price"] = ''
			fields["new_price"] = float(option.new_price)
			fields["cashback"] = float(offer.percent_cashback)
			fields["discount"] = float(option.discount())
			fields["remaining"] = option.time_remaining()
			fields["quantity"] = int(offer.bought + offer.bought_virtual)
			data.append(fields)
		return data

class Offer(models.Model):
	title = models.CharField(u'Título', max_length=255)
	slug = models.SlugField(max_length=255, unique=True, blank=True)
	image_grid = models.ImageField(verbose_name=u'Imagem do gride', upload_to='oferta/')
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

	my_first_option = None

	objects = OfferManager()

	class Meta:
		verbose_name = u'Oferta'
		verbose_name_plural = u'Ofertas'

	def __unicode__(self):
		return self.title

	@property
	def partner(self):
		return self.options.select_related('filial__partner').all()[0].filial.partner

	def bought_total(self):
		return self.bought + self.bought_virtual

	def first_option(self):
		if self.my_first_option is not None:
			return self.my_first_option
		self.my_first_option = self.options.select_related('filial__partner').filter(start_time__lte=datetime.today(), end_time__gte=datetime.today()).order_by('new_price')[0]
		return self.my_first_option

	def other_options(self):
		return self.options.select_related('filial__partner').all().exclude(id=self.first_option().id)

	def related_offers(self):
		return Offer.objects.select_related('city').filter(options__start_time__lte=datetime.today(), options__end_time__gte=datetime.today()).exclude(id=self.id).annotate(count=Count('id')).order_by('-count')

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
	subtitle = models.CharField(u'Sub Título', max_length=255)
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
		return 100 - (100 * self.new_price / self.old_price)

	def time_remaining(self):
		date = self.end_time - timezone.now()
		# return datetime.strptime(date, "%a %b %d %H:%M:%S %Z %Y")
		return "%sd %.2d:%.2d:%.2d" % (date.days,date.seconds//3600,(date.seconds//60)%60, date.seconds%60)


class PromotionCode(models.Model):
	code = models.CharField(u'Código', max_length=255)
	discount = models.DecimalField(u'Desconto', decimal_places=2, max_digits=10)
	start_time = models.DateTimeField(u'Começa em')
	end_time = models.DateTimeField(u'Termina em')

	def __unicode__(self):
		return self.code

	def is_available(self):
		today = timezone.now()
		if today >= self.start_time and today < self.end_time:
			return True
		return False