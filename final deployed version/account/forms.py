from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm  #this also auth app usercreation form
from django.contrib.auth.models import User   # this is improting django auth app user model 
from django import forms 

from store.models import *


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User  #accessing the user model 
		fields = ['username', 'email', 'password1', 'password2']   # this the attribute we get for user creation this names are got from django manual
		