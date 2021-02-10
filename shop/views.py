from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    # n = len(products)
    # num_slides = n//4 + ceil((n/4)-(n//4))
    # params = {'products': products, 'num_slides': num_slides, 'range': range(1, num_slides)}
    # allProds = [[products, range(1, num_slides), num_slides], [products, range(1, num_slides), num_slides]]
    allProds = []
    catprods= Product.objects.values('sub_category', 'id')
    cats= {item["sub_category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(sub_category=cat)
        n = len(prod)
        num_slides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, num_slides), num_slides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    # return HttpResponse("Hello from Django.")
    return render(request, 'shop/about.html')


def contact(request):
    # return HttpResponse("Hello from Django.")
    if request.method ==  'POST':
        print(request)
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, desc=message)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse("Hello from Django.")


def search(request):
    return HttpResponse("Hello from Django.")


def productview(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'shop/product.html', {'product': product[0]})


def checkout(request):
    return HttpResponse("Hello from Django.")

