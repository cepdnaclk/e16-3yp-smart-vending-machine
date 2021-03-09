from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [

	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
         
	path('home/', views.home, name="home"),  #home path
	path('user/', views.userPage, name="user-page"),

	path('accountSettings/', views.accountSettings, name="accountSettings"),

	path('products/', views.products,name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),


    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateProduct , name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct , name="delete_product"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), 
        name="password_reset_complete"),
	 
]

 