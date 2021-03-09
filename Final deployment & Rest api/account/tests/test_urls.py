from django.test import SimpleTestCase
from django.test import TestCase

from django.urls import reverse ,resolve 

from account.views import *

class TestUrls(SimpleTestCase):
	def test_register_urls_is_resolve(self):
		url= reverse ('register')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,registerPage)

	def test_login_urls_is_resolve(self):
		url= reverse ('login')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,loginPage)

	def test_logout_urls_is_resolve(self):
		url= reverse ('logout')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,logoutUser)

	def test_home_urls_is_resolve(self):
		url= reverse ('home')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,home)

	def test_user_page_urls_is_resolve(self):
		url= reverse ('user-page')
		# print(resolve(url))
		self.assertEquals(resolve(url).func,userPage)