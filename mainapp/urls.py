from django.contrib import admin
from django.urls import path
from mainapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('addcustomer/', views.Customeradd, name="addcustomer"),
    path('customer/<str:pk>/', views.customerview, name="customer"),
    path('create_collection<str:pk>/', views.create_collection, name="create_collection"),
    path('update_collection/<str:pk1>/', views.update_collection, name="update_collection"),
    path('delete_collection/<str:pk1>/', views.delete_collection, name="delete_collection"),
    path('update_customer/<str:pk>/', views.update_customer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete_customer"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"), 
        name="password_reset_complete"),
]

# Submit Email form ----------------------- PasswordResetView.as_view()
# Email Success message ------------------- PasswordResetDoneView.as_view()
# Link to password change in Email -------- PasswordResetConfirmView.as_view()
# Password successfully change message ---- PasswordResetCompleteView.as_view()