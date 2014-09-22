# coding:utf-8
from django.db import models
from account.models import OferClubUser
from offer.models import Option
from account.models import Address

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

    option = models.ForeignKey(Option, related_name='orders')

    quantity = models.IntegerField(u'Quantidade', default=1)

    total = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor pago')

    status = models.PositiveSmallIntegerField(null=True, blank=True, choices=STATUS_CHOICES, default=2, verbose_name=u'situação')

    purchase_time = models.DateTimeField(auto_now_add=True, verbose_name=u'data')

    @property
    def authorized(self):
        return self.status == ORDER_AUTHORIZED

    @property
    def parsed_total(self):
        return "%0.2f" % self.total

    def __unicode__(self):
        return u"%s - %s" % (self.user.full_name, self.parsed_total)

    class Meta:
        ordering = ["purchase_time"]
        verbose_name = u"Pedido"
        verbose_name_plural = u"Pedidos"
        app_label = 'checkout'


class Coupon(models.Model):
    order = models.ForeignKey(Order, related_name='get_coupons')
    name_consumer = models.CharField(max_length=200, verbose_name=u'nome completo')
    code = models.CharField(u'Código', max_length=255, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor pago')
    is_consumed = models.BooleanField(u'Foi consumido?', choices=CONSUME, default=NOT_CONSUMED)
    address = models.ForeignKey(Address, blank=True, null=True, verbose_name=u'endereço')
    date_expiration = models.DateField(u'Expira em')
    date_consumed = models.DateTimeField(auto_now_add=True, verbose_name=u'Consumido em')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=u'Gerado em')

    def __unicode__(self):
        return "%s - %s" % (self.name_consumer, self.code)

    class Meta:
        ordering = ["date_created"]
        verbose_name = u"Cupom"
        verbose_name_plural = u"Cupons"
        app_label = 'checkout'

DEBIT = 0
CREDIT = 1
TYPES = (
    (DEBIT, 'Débito'),
    (CREDIT, 'Crédito')
    )

class Operation(models.Model):
    user = models.ForeignKey(OferClubUser, verbose_name=u'usuário', related_name='operations')
    type_operation = models.BooleanField(u'Tipo', choices=TYPES, default=DEBIT)
    value = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'valor')
    total = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=u'total')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Gerado em')

    class Meta:
        verbose_name = u'Operação'
        verbose_name_plural = u'Operações'

    def __unicode__(self):
        if self.type_operation:
            type_operation = 'Crédito'
        else:
            type_operation = 'Débito'
        return '%s - R$%.2f (%s)' % (self.user.full_name, self.value, type_operation)