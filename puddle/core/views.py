from django.shortcuts import render, redirect
# import models for displaying objects where applicable on frontend app
from item.models import Category, Item
# import forms
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=0)[0:6]
    categories = Category.objects.all()
    # return render(request, 'core/index.html')
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('') 
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

