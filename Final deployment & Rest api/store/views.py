from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
import qrcode 
from io import BytesIO
from django.core.files import File 
from  PIL  import Image ,ImageDraw 
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# from django.contrib.auth.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout  # this for login and logout methods provied by django
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage

# Create your views here.

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	product_paginator=Paginator(products,3)

	page_number = request.GET.get('page',1)
	try:
		page=product_paginator.get_page(page_number)
	except EmptyPage:
		page=product_paginator.page(1)

	context = {'products':page, 'cartItems':cartItems}
	return render(request, 'store/Store.html', context)




def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/Cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/Checkout.html', context)



# @csrf_exempt								
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


@csrf_exempt
def processQR(request):
	context={}
	if request.method == 'POST':

		data1 = json.loads(request.body)
		name = data1['form']['name']
		email = data1['form']['email']
		if request.user.is_authenticated:
			customer = request.user.customer
		else:
			try:
				customer=Customer.objects.get(email=email,name=name)
			except Exception as e:
				return JsonResponse('', safe=False)
			

		orders = Order.objects.filter(customer=customer, status='Pending')
		print(orders)
		dic=list()
		for order in orders:
			shippingAddress = ShippingAddress.objects.filter(order=order )
			if len(shippingAddress)>0:
				dic.append(shippingAddress[0].qr_code.url) 
				print(shippingAddress[0],'that qr')
	 
		context = {'dic':dic}
		out=json.dumps(dic)

		return JsonResponse(dic, safe=False)

	if request.user.is_authenticated:
		customer1 = request.user.customer
		orders = Order.objects.filter(customer=customer1, status='Pending')
		print(orders)
		dic=list()
		print('hi')
		for order in orders:
			shippingAddress = ShippingAddress.objects.filter(order=order )
			if len(shippingAddress)>0:
				dic.append(shippingAddress[0]) 
				print(shippingAddress[0],'that qr')
	 
		context = {'dic':dic}


	return render(request, 'store/QR.html',context)
@csrf_exempt
def processOrder(request):
	if request.method == 'POST':
		transaction_id = datetime.datetime.now().timestamp()
		data = json.loads(request.body)

		if request.user.is_authenticated:
			customer = request.user.customer
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
		else:
			customer, order = guestOrder(request, data)
			

		total = float(data['form']['total'])
		order.paidAmount=total
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
			order.status='Pending'
		order.save()

		if order.shipping == True:
			orderDate=order.date_ordered
			transactionComplete=order.complete 
			transactionstatus=order.status
			customerName=customer.name
			customerEmail=customer.email
			items =OrderItem.objects.filter(order=order )
			orderProductes ={}

			for item in items:
				orderProductes[item.product.name]=item.quantity
				item.product.available=item.product.available-item.quantity
				item.save()


			amountTopay=order.get_cart_total
			num=order

			paid_amount=total

			shipInfo={
				"orderDate":str(orderDate),
				"transactionComplete":transactionComplete,
				"transactionstatus":transactionstatus,
				"customerName":customerName,
				"customerEmail":customerEmail,
				"orderProductes":orderProductes,
				"amountTopay":amountTopay,
				"paid_amount":paid_amount,
				"transaction_id":transaction_id	,
				"Id":str(num),
			}


			QR_data=json.dumps(shipInfo) 

			qr_img=qrcode.make(QR_data)
			Fname=f'qrcode-{customer.name}-{order.transaction_id}.png'
			image=qrcode.make(QR_data)

			# canvas=Image.new('RGB',(1000,1000),'white')
			# draw=ImageDraw.Draw(canvas)
			# canvas.paste(qr_img)
			buffer=BytesIO()
			qr_img.save(buffer,'PNG')
			print(buffer)



			ShippingAddress.objects.create(
			customer=customer,
			order=order,
			qr_code=image.save(Fname)
			
			)
			shipp = ShippingAddress.objects.get(customer=customer,order=order)
			shipp.qr_code.save(Fname,File(buffer))
			print(shipp.qr_code)
			# canvas.close()
		return JsonResponse('Payment submitted..', safe=False)


	


	# def processQR(request):

	# 	return render(request, 'store/QR.html')



	