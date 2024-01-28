from django.http import HttpResponse
from django.shortcuts import render
from viewer.models import Product, ShowSector


def prove(request):
    products = Product.objects.all()
    return render(request, template_name="home.html", context={"products": products})

def is_valid_query(para):
    return para is not None and len(para) > 0

def search(request):
    products = Product.objects.all().order_by("-date")
    name = request.GET.get("product-name")
    if is_valid_query(name):
        products = Product.objects.filter(name__icontains=name)

    return render(request, template_name="search.html", context={"products": products})
