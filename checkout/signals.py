# -*- coding: utf-8 -*-
from django.dispatch.dispatcher import Signal


def receiver_post_save(sender, instance, created, **kwargs):
	from checkout.models import Operation, CREDIT, DEBIT, Coupon, ORDER_AUTHORIZED
	from datetime import datetime

	# debits balance
	if created and instance.option.new_price * instance.quantity > instance.total:
		diff_value = instance.option.new_price * instance.quantity - instance.total
		Operation.objects.create(user=instance.user, type_operation=DEBIT, description=instance.option.title, value=diff_value)

	if instance.status == ORDER_AUTHORIZED and not instance.date_approved:
		# generate coupons
		for i in range(instance.quantity):
			Coupon.objects.create(order=instance, price=instance.option.new_price, date_expiration=instance.option.date_expiration)
			instance.option.offer.bought += 1
			instance.option.quantity -= 1

		instance.option.offer.save()
		instance.option.save()

		# generate cashback
		if instance.option.offer.percent_cashback > 0 and instance.total > 0:
			value = instance.total * instance.option.offer.percent_cashback / 100
			Operation.objects.create(user=instance.user, type_operation=CREDIT, description='CashBack', value=value)
		
		instance.date_approved = datetime.today()
		instance.save()


def update_credit(sender, instance, created, **kwargs):
	from checkout.models import CREDIT
	if created:
		if instance.type_operation == CREDIT:
			instance.user.credit = instance.user.credit + instance.value
		else:
			instance.user.credit = instance.user.credit - instance.value
		instance.user.save()