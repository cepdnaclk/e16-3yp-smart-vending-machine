from django.urls import path

from . import views

urlpatterns = [
         
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('process_QR/', views.processQR, name="process_QR"),
	# path('process_QR_post/', views.processQR_post, name="process_QR_post"),

]