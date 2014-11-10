# coding:utf-8
import time
import hashlib
import random
from pagseguro import PagSeguro
from django.db.models.signals import post_save
from django.db import models
from account.models import OferClubUser
from offer.models import Option
from account.models import Address
from .signals import receiver_post_save, update_credit, coupon_save
from datetime import date

# Create your models here.

ORDER_AUTHORIZED = 0

STATUS_CHOICES = (
    (ORDER_AUTHORIZED, u'Aprovada'),
    (1, u'Negada'),
    (2, u'Em Análise'),
)

CONSUMED = 1
NOT_CONSUMED = 0
CONSUME = (
	(CONSUMED, U'Consumido'),
	(NOT_CONSUMED, U'Não Consumido'),
)


class Order(models.Model):
    """
        Representação de um pedido.
    """
    user = models.ForeignKey(OferClubUser, verbose_name=u'usuário', related_name='orders')

    total = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor pago')

    shipping = models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=u'Frete')

    discount = models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=u'Desconto')

    balance = models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=u'Saldo usado')

    code_pagseguro = models.CharField(u'Código PagSeguro', max_length=255, blank=True, null=True)

    status = models.PositiveSmallIntegerField(null=True, blank=True, choices=STATUS_CHOICES, default=2, verbose_name=u'situação')

    address = models.ForeignKey(Address, blank=True, null=True, verbose_name=u'endereço')

    purchase_time = models.DateTimeField(auto_now_add=True, verbose_name=u'data')

    date_approved = models.DateTimeField(u'Aprovado em', blank=True, null=True)

    class Meta:
        ordering = ["purchase_time"]
        verbose_name = u"Pedido"
        verbose_name_plural = u"Pedidos"
        app_label = 'checkout'

    @property
    def authorized(self):
        return self.status == ORDER_AUTHORIZED

    @property
    def parsed_total(self):
        return "%0.2f" % self.total

    def __unicode__(self):
        return u"%s - %s" % (self.user.full_name, self.parsed_total)


    def pay_pagseguro(self):
        # import pdb;pdb.set_trace()
        pg = PagSeguro(email="victorluna22@gmail.com", token="4194D1DFC27E4E1FAAC0E1B20690B5B5")
        pg.sender = {
            "name": self.user.full_name,
            "email": self.user.email,
        }
        pg.reference_prefix = None
        pg.reference = self.id
        pg.add_item(id=self.option.id, description=self.option.title, amount=self.total, quantity=1, weight=0)
        # pg.redirect_url = "http://meusite.com/obrigado"
        response = pg.checkout()
        self.code_pagseguro = response.code
        self.save()
        return response.payment_url

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='itens')
    name_consumer = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'nome completo')
    option = models.ForeignKey(Option, related_name='orders')
    quantity = models.IntegerField(u'Quantidade', default=1)
    total = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor pago')

    def __unicode__(self):
        return "%s (%s)" % (self.name_consumer, self.total)

# class Gift(models.Model): DESENVOLVER

class Coupon(models.Model):
    order_item = models.ForeignKey(OrderItem, related_name='cupons')
    code = models.CharField(u'Código', max_length=255, unique=True)
    name_consumer = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'nome completo')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor pago')
    is_consumed = models.BooleanField(u'Foi consumido?', choices=CONSUME, default=NOT_CONSUMED)
    date_expiration = models.DateField(u'Expira em')
    date_consumed = models.DateTimeField(blank=True, null=True, verbose_name=u'Consumido em')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u'Gerado em')


    class Meta:
        ordering = ["date_created"]
        verbose_name = u"Cupom"
        verbose_name_plural = u"Cupons"
        app_label = 'checkout'

    def __unicode__(self):
        return "%s - %s" % (self.name_consumer, self.code)

    def _createHash(self):
        """This function generate 10 character long hash"""
        hash = hashlib.sha1()
        hash.update(str(time.time()))
        hashstr = hash.hexdigest()[:12] + str(self.order_item.id) + str(random.randint(0,9))
        return hashstr.upper()

    def get_status(self):
        today = date.today()

        if self.is_consumed:
            return 'consumido'
        elif today > self.date_expiration:
            return 'vencido'
        else:
            return 'disponível'

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self._createHash()
        return super(Coupon, self).save(*args, **kwargs)


DEBIT = 0
CREDIT = 1
TYPES = (
    (DEBIT, 'Débito'),
    (CREDIT, 'Crédito')
    )

class Operation(models.Model):
    user = models.ForeignKey(OferClubUser, verbose_name=u'usuário', related_name='operations')
    description = models.CharField(u'Descrição', max_length=255)
    type_operation = models.BooleanField(u'Tipo', choices=TYPES, default=DEBIT)
    value = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Gerado em')

    class Meta:
        verbose_name = u'Operação'
        verbose_name_plural = u'Operações'

    def __unicode__(self):
        if self.type_operation:
            type_operation = u'Crédito'
        else:
            type_operation = u'Débito'
        return u'%s - R$%.2f (%s)' % (self.user.full_name, self.value, type_operation)


post_save.connect(receiver_post_save, sender=Order, dispatch_uid='checkout.signals.post_save')
post_save.connect(update_credit, sender=Operation, dispatch_uid='checkout.signals.post_save')
post_save.connect(coupon_save, sender=Coupon, dispatch_uid='checkout.signals.post_save')