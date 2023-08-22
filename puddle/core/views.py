from django.shortcuts import render
# import models for displaying objects where applicable on frontend app
from item.models import Category, Item

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

