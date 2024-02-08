from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def supplierlistview(request):
    return render(request, 'supplierlist.html')

def productlistview(request):
    return render(request, 'productlist.html')


# Create your views here.
