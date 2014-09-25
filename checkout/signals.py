# -*- coding: utf-8 -*-
from django.dispatch.dispatcher import Signal


def generate_coupon(sender, instance, created, **kwargs):
	from checkout.models import Coupon
	if created:
		for i in range(instance.quantity):
			Coupon.objects.create(order=instance, price=instance.option.new_price, date_expiration=instance.option.date_expiration)



def generate_cashback(sender, instance, created, **kwargs):
	from checkout.models import Operation, CREDIT
	if created and instance.option.offer.percent_cashback > 0:
		value = instance.total * instance.option.offer.percent_cashback / 100
		Operation.objects.create(user=instance.user, type_operation=CREDIT, description='CashBack', value=value)


def update_credit(sender, instance, created, **kwargs):
	from checkout.models import CREDIT
	if created:
		if instance.type_operation == CREDIT:
			instance.user.credit = instance.user.credit + instance.value
		else:
			instance.user.credit = instance.user.credit - instance.value
		instance.user.save()