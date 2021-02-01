from django.test import SimpleTestCase
from django.test import TestCase,  Client
from django.contrib.auth.models import User

from account.forms import ProductForm  ,CreateUserForm ,CustomerForm 

from django.urls import reverse ,resolve 
from store.models import Customer,Product,Order,OrderItem,ShippingAddress




class formTestUrls(TestCase):


	def test_CreateUserForm_valid_data(self):
		form= CreateUserForm(data={
							'username':'hari',
							'email':'hari@gmail.com',
							'password1':'test12345',
							'password2':'test12345'

							})

		self.assertTrue(form.is_valid())
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		self.assertEquals(username,'hari')
		self.assertEquals(email,'hari@gmail.com')


	def test_ProductForm_valid_data(self):
		form= ProductForm(data={
							'name':'milk',
							'price':'24',
							'image':' ',
							'available':'4',
							'place':'row a'

							})
		self.assertTrue(form.is_valid())


	def test_CustomerForm_valid_data(self):
		form= CustomerForm(data={
							'name':'hari',
							'email':'hari@gmail.com',
							'phone':'0778877953 ',
							'profile_pic':''
							  

							})
		response =self.client.post(reverse('accountSettings'),{'form':{
							'name':'hari',
							'email':'hari@gmail.com',
							'phone':'0778877953 ',
							'profile_pic':''
							  

							} })

		self.assertEquals(response.status_code,302)
		self.assertTrue(form.is_valid())
		