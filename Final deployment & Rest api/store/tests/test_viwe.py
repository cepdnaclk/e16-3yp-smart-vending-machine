from django.test import SimpleTestCase
from django.test import TestCase,  Client
from django.contrib.auth.models import User

from store.models import Customer,Product,Order,OrderItem,ShippingAddress

from django.urls import reverse ,resolve 


class storeTestViews(TestCase):

	def setUp(self):
		self.client=Client()
		self.update_item_url=reverse('update_item')
		self.user=User.objects.create(username='kaml')
		self.customer=Customer.objects.create(user=self.user,name=self.user.username)
		self.product = Product.objects.create(id=1,name='milk',price=25)
		self.order= Order.objects.create(customer=self.customer, complete=False)
		self.orderItem= OrderItem.objects.create(order=self.order, product=self.product,quantity=0)


	def test_store_GET(self):
		

		response =self.client.get(reverse('store'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'store/Store.html')


	def test_cart_GET(self):
		

		response =self.client.get(reverse('cart'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'store/Cart.html')


	def test_checkout_GET(self):
		

		response =self.client.get(reverse('checkout'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'store/Checkout.html')


	def test_updateItem_POST_without_arg(self):
		

		response =self.client.post(reverse('update_item'))

		self.assertEquals(response.status_code,200)
		# self.assertTemplateUsed(response,'store/Checkout.html')

	def test_updateItem_POST_arg(self):
		

		response =self.client.post(reverse('update_item'),{'productId':1, 'action':'remove'})

		self.assertEquals(response.status_code,200)
		self.assertEquals(self.orderItem.quantity,0)
		print(self.orderItem.product.id,'this',self.orderItem.quantity)


	def test_processQR_GET(self):
		

		response =self.client.get(reverse('process_QR'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'store/QR.html')


	def test_processQR_POST_without_arg(self):
		

		response =self.client.post(reverse('process_QR'))

		self.assertEquals(response.status_code,200)
		# self.assertTemplateUsed(response,'store/Checkout.html')


	def test_processQR_POST_arg(self):
		customer1=Customer.objects.create(name='kari',email='kari@gmail.com')

		response =self.client.post(reverse('process_QR'),{'form':{ 'name':'kari','email':'kari@gmail.com'} })

		self.assertEquals(response.status_code,200)
		print(response.content,'oooooooo')
		# self.assertEquals(self.orderItem.quantity,0)
		# print(self.orderItem.product.id,'this',self.orderItem.quantity)


	def test_processOrder_GET(self):
		

		response =self.client.get(reverse('process_order'))

		self.assertEquals(response.status_code,200)
		print(response.content)
		# self.assertTemplateUsed(response,'store/QR.html')