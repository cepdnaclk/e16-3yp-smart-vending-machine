from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout  # this for login and logout methods provied by django

from django.contrib.auth.decorators import login_required  #this for allwing the only for login user 
from django.contrib import messages  # this also provieded for throwing flash messages 
from django.contrib.auth.models import Group
 
# Create your views here.
from .models import *   # imprting all database models for viwe 
from .form import OrderForm,CreateUserForm    # imporing this forms 
from .filters import OrderFilter       # for seching attribute provieded by this 
from .decorators import unauthenticated_user, allowed_users, admin_only  # this inport the decoreters

@login_required(login_url='login')
@admin_only
def home(request):
	orders = Order.objects.all()    #takeing all obj of orders 
	customers = Customer.objects.all()  # taking all object of customers 

	total_customers = customers.count()    # taking customer obj count 

	total_orders = orders.count()  # taking customer obj count 
	delivered = orders.filter(status='Delivered').count()   # useing filter quary method to counting the specific stats
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers, #passing the all value to the page as context
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'accouts/dashboard.html', context)  #rendering the dashbord 


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()   # taking all obj of products 

	return render(request, 'accouts/products.html', {'products':products})


@unauthenticated_user
def loginpath(request):


	if request.method=='POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')
			return render(request, 'accouts/login.html')
	  

	context={}
	return render(request, 'accouts/login.html',context)
	 

	
@unauthenticated_user
def register(request):
	 
	form=CreateUserForm()
		
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
 
	context={'form':form}
	return render(request, 'accouts/register.html',context)


def logoutUser(request):
	logout(request)
	return redirect('login')

def userPage(request):
	context={}
	return render(request, 'accouts/user.html',context)



@login_required(login_url='login')    # login user only can acess this page 
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accouts/order_form.html', context)

@login_required(login_url='login')    # login user only can acess this page 
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	# form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		# form = OrderForm(request.POST,instance=customer)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset,'customer':customer}
	return render(request, 'accouts/order_form.html', context)


@login_required(login_url='login')    # login user only can acess this page 
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accouts/delete.html', context)

@login_required(login_url='login')     # login user only can acess this page 
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accouts/customer.html',context)