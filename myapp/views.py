# views.py

from django.shortcuts import render
from .models import ProductMst, ProductSubCategory

def index(request):
    subcategories = ProductSubCategory.objects.all()

    # Handle search query
    query = request.GET.get('search')
    if query:
        subcategories = subcategories.filter(product__product_name__icontains=query)

    return render(request, 'home.html', {'subcategories': subcategories})
