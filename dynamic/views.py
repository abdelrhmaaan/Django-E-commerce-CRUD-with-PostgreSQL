from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from . import models as m
# Create your views here.

def home(request):
    products = m.Product.objects.all()
    images= [
        {'image':'images/pic1.jpg'},
        {'image':'images/pic2.jpg'},
        {'image':'images/pic3.jpg'},
            ]
    return render(request,'pages/home.html',context={'products': products,'images':images})

def any(request):
    return HttpResponse('<h1>Hello, Django</h1>')

def go(request):
    return render(request,'h.html')

def contact(request):
    return render(request,'pages/contact.html')

def aboutus(request):
    return render(request,'pages/about.html')

def productpage(request,id):
    product = m.Product.objects.get(id=id)
    return render(request,'pages/productpage.html',context={'product':product})

def delete(request,id):
    deleted_product = m.Product.objects.get(id=id)
    deleted_product.delete()
    return redirect('home')

def search(request):
    search_term = request.POST.get('search_term')
    filtered_products = m.Product.objects.filter(name__contains = search_term)
    return render(request,'pages/search.html',context={'filtered_products': filtered_products})

def create(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    # image = request.POST.get('image')
    image = request.FILES.get('image')
    newProdcut = m.Product()
    newProdcut.name = name
    newProdcut.price = price
    newProdcut.image = image
    if newProdcut.name and newProdcut.price and newProdcut.image:
        newProdcut.save()
        return redirect('create')
    return render(request,'pages/create.html')

def edit(request,id):
    editedProdcut = m.Product.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        # image = request.POST.get('image')
        image = request.FILES.get('image')
        editedProdcut.name = name
        editedProdcut.price = price
        editedProdcut.image = image
        if editedProdcut.name and editedProdcut.price and editedProdcut.image:
            editedProdcut.save()
            return redirect('home')
    return render(request,'pages/edit.html',context={'eproduct':editedProdcut})

def category(request,cat_name):
    cat = m.Category.objects.get(name = cat_name)
    products = m.Product.objects.filter(category=cat.id)
    # print(products)
    return render(request,'pages/category.html',context={'category':cat,'products':products})

# make table ==> insert data into the table 
# retrieve data from the table 
