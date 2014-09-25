# conding: utf-8
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('quantity',)

	# def save(self, *args, **kwargs):
	# 	import pdb;pdb.set_trace()
	# 	return super(OrderCreateForm, self).save(*args, **kwargs)