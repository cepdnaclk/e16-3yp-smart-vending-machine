from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout  # this for login and logout methods provied by django

from django.contrib.auth.decorators import login_required  #this for allwing the only for login user 
from django.contrib import messages  # this also provieded for throwing flash messages 
from django.contrib.auth.models import Group
 
# Create your views here.
from store.models import *   # imprting all database models for viwe 
from .forms import ProductForm  ,CreateUserForm ,CustomerForm   # imporing this forms 
from .filters import OrderFilter ,ProductFilter      # for seching attribute provieded by this 
from .decorators import unauthenticated_user, allowed_users, admin_only  # this inport the decoreters

# Create your views here.

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			 

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			Customer.objects.create(user=user,name=user.username)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'account/register.html', context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		 

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if request.user.is_staff:
				return redirect('home')
			else:
				return redirect('store')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'account/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'account/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order= Order.objects.get(customer=customer, complete=False)
		# items = 0#OrderItem.objects.get(order=order)
		cartItems = order.get_cart_items
		orders = request.user.customer.order_set.all()

		total_orders = orders.count()
		delivered = orders.filter(status='Delivered').count()
		pending = orders.filter(status='Pending').count()
		# print(items)
		prodect=list()
		for order in orders:
			items=OrderItem.objects.filter(order=order )
			for i in range(len(items)):
				prodect.append(items[i]) 
				print(items[0])

		cartItems = order.get_cart_items
	context = {'cartItems':cartItems,'orders':orders ,'total_orders':total_orders,
	'delivered':delivered,'pending':pending,'prodect':prodect}
	return render(request, 'account/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	if request.user.is_authenticated:
		customer = request.user.customer
		order= Order.objects.get(customer=customer, complete=False)
		cartItems = order.get_cart_items

	context = {'form':form,'cartItems':cartItems}
	return render(request, 'account/account_settings.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()

	myFilter = ProductFilter(request.GET, queryset=products)   # add to the filter django method 
	products = myFilter.qs 
	context = {'products':products,   'myFilter':myFilter}
	return render(request, 'account/products.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)   # add to the filter django method 
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
	print('data:',context)
	return render(request, 'account/customer.html',context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createProduct (request):
	form = ProductForm()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('products')

	context = {'form':form}
	return render(request, 'account/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateProduct(request, pk):  #updatein the specific order for useing pk as id 

	product = Product.objects.get(id=pk)   #geting the currsponding order object
	form = ProductForm(instance=product)   # free filed form for passin the instance 

	if request.method == 'POST':    # get the update data and store to the data base 
		form = ProductForm(request.POST, request.FILES ,instance=product)
		if form.is_valid():
			form.save()
			return redirect('products') #then send to the home page 

	context = {'form':form} # if the get method we sending the form to page 
	return render(request, 'account/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('products')

	context = {'item':product}
	return render(request, 'account/delete.html', context)
