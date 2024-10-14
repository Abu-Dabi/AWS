from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from .models import *


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def contacts(request):
    return render(request, 'contacts.html')


def item_list(request, id):
    items = Item.objects.filter(category=id)
    return render(request, 'items.html', {'items': items})


def item_detail(request, id):
    item = Item.objects.get(id=id)
    images = ItemImage.objects.filter(recept=id)
    return render(request, 'item_detail.html', {'item': item, 'images': images})


def site_register(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    except ValueError:
        return redirect('/register/')


def site_login(request):
    try:
        if request.method == 'POST':
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return redirect('/')
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})
    except AttributeError:
        return redirect('/register/')


def site_logout(request):
    logout(request)
    return redirect('/')


