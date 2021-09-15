from django.forms import ModelForm
from mainapp.models import Collection, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CollectionForm(ModelForm):

    class Meta:
        model = Collection
        fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address']
