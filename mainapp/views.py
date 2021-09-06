from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.models import Customer, Collection
from mainapp.forms import CollectionForm, CreateUserForm, CustomerForm
from mainapp.filters import CollectionFilter, CustomerFilter

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def index(request):
    customers = request.user.Customer.all()
    total_customers = request.user.Customer.all().count()

    customerfilter = CustomerFilter(request.GET, queryset=customers)
    customers = customerfilter.qs

    context = {'customers':customers, 'customerfilter': customerfilter, 'total_customers':total_customers}
    return render(request, 'dashboard.html', context)

def Customeradd(request):
    context = {}
    customers = Customer.objects.all()
    form = CustomerForm()
    if request.POST:
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            request.user.Customer.add(instance)
            return redirect('home')


    context = {'form': form}
    return render(request, 'create_customer.html', context)

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.POST:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'customer': customer, 'form': form}
    return render(request, 'update_customer.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.POST:
        customer.delete()
        return redirect('home')
    context = {'customer': customer}
    return render(request, 'delete_customer.html', context)

def customerview(request, pk):
    customer = Customer.objects.get(id=pk)
    collections = customer.collection_set.all()

    myfilter = CollectionFilter(request.GET, queryset=collections)
    collections = myfilter.qs

    context = {'customer':customer, 'collections':collections, 'myfilter': myfilter}
    return render(request, 'customer.html', context)

def create_collection(request, pk):
    customer = Customer.objects.get(id=pk)

    form = CollectionForm(initial={'customer': customer})
    if request.POST:
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            request.user.collections.add(form)
            

    context = {'form':form, 'customer': customer}
    return render(request, 'create_collection.html', context)

def update_collection(request, pk1):
    collection = Collection.objects.get(id=pk1)
    form = CollectionForm(instance=collection)
    if request.POST:
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form, 'collection':collection}
    return render(request, 'updatecollection.html', context)

def delete_collection(request, pk1):
    collection = Collection.objects.get(id=pk1)

    if request.POST:
        collection.delete()
        return redirect('home')
    
    context = {'collection': collection}
    return render(request, 'delete_collection.html', context)

