# -*- coding: utf-8 -*-
from django.dispatch.dispatcher import Signal


def receiver_post_save(sender, instance, created, **kwargs):
	from checkout.models import Operation, CREDIT, DEBIT, Coupon, ORDER_AUTHORIZED, NOT_CONSUMED
	from datetime import datetime

	if instance.status == ORDER_AUTHORIZED and not instance.date_approved:
		# generate coupons
		for item in instance.itens.all():
			for i in range(item.quantity):
				Coupon.objects.create(order_item=item, name_consumer=item.name_consumer, is_consumed=NOT_CONSUMED, price=item.option.new_price, date_expiration=item.option.date_expiration)

		# generate cashback
		if item.option.offer.percent_cashback > 0 and instance.total > 0:
			value = instance.total * item.option.offer.percent_cashback / 100
			Operation.objects.create(user=instance.user, type_operation=CREDIT, description='CashBack', value=value)
		
		instance.date_approved = datetime.today()
		instance.save()


def update_credit(sender, instance, created, **kwargs):
	from checkout.models import CREDIT
	if created:
		if instance.type_operation == CREDIT:
			instance.user.credit = float(instance.user.credit) + float(instance.value)
		else:
			instance.user.credit = float(instance.user.credit) - float(instance.value)
		instance.user.save()


def coupon_save(sender, instance, created, **kwargs):
	if created:
		instance.order_item.option.offer.bought += 1
		instance.order_item.option.quantity -= 1

		instance.order_item.option.offer.save()
		instance.order_item.option.save()