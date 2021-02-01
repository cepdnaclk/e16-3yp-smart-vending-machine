from django.test import SimpleTestCase
from django.test import TestCase,  Client
from django.contrib.auth.models import User

from store.models import Customer,Product,Order,OrderItem,ShippingAddress

from django.urls import reverse ,resolve 


class accountTestViews(TestCase):

	def setUp(self):
		self.client=Client()
		self.update_item_url=reverse('update_item')
		self.user=User.objects.create(username='kaml')
		self.customer=Customer.objects.create(user=self.user,name=self.user.username)
		self.product = Product.objects.create(id=1,name='milk',price=25)
		self.order= Order.objects.create(customer=self.customer, complete=False)
		self.orderItem= OrderItem.objects.create(order=self.order, product=self.product,quantity=0)


	def test_registerPage_GET(self):
		

		response =self.client.get(reverse('register'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'account/register.html')



	def test_registerPage_POST_without_arg(self):
		

		response =self.client.post(reverse('register'))

		self.assertEquals(response.status_code,200)
		print(response)
		# self.assertTemplateUsed(response,'store/Checkout.html')