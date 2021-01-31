from django.test import SimpleTestCase
from django.test import TestCase

from django.urls import reverse ,resolve 

from store.views import updateItem,checkout,store,cart,processOrder

class TestUrls(SimpleTestCase):
	def test_store_urls_is_resolve(self):
		url= reverse ('store')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,store)

	def test_cart_urls_is_resolve(self):
		url= reverse ('cart')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,cart)

	def test_checkout_urls_is_resolve(self):
		url= reverse ('checkout')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,checkout)

	def test_update_item_urls_is_resolve(self):
		url= reverse ('update_item')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,updateItem)

	def test_processOrder_urls_is_resolve(self):
		url= reverse ('process_order')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,processOrder)

