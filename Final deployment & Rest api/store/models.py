from django.db import models
from django.contrib.auth.models import User

import qrcode 
 

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200, null=True)
	profile_pic= models.ImageField(default= "profile1.png"	,null=True,blank=True)


	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	# digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(default= "placeholder.png", null=True, blank=True)
	available = models.IntegerField(default=0, null=True, blank=True)
	place = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Order(models.Model):
	STATUS = (
			('Not paid', 'Not paid'),
			('Pending', 'Pending'),
			 
			('Delivered', 'Delivered'),
			)
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	paidAmount = models.IntegerField(default=0, null=True, blank=True)
	transaction_id = models.CharField(max_length=100, null=True)
	status = models.CharField(default='Not paid',max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.id)

	@property                    #this the function getting the total bill amount 
	def get_cart_total(self):
		orderitems = OrderItem.objects.filter(order=self)  #this object give all iterms own by the order 
		total = sum([item.get_total for item in orderitems])   #this is calculating all iterms total through the loop 
		return total 

	@property
	def get_cart_items(self):
		orderitems = OrderItem.objects.filter(order=self)
		total = sum([item.quantity for item in orderitems])
		return total 

	@property
	def shipping(self):
		shipping = True
		 
		return shipping

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL,related_name='OrderItems', null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.date_added)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	qr_code=models.ImageField(null=True,blank=True)



	def __str__(self):
		return str(self.qr_code)