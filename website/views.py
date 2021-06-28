from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def cart(request):
    return render(request, "cart.html", locals())

def checkout(request):
    return render(request, "checkout.html", locals())

def produitDetails(request):
    return render(request, "product-details.html", locals())

def shop(request):
    return render(request, "shop.html", locals())