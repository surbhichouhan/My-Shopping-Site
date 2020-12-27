from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
import json


def home(request):
    #products = Product.objects.all()
    #n = len(products)
    #nslide = ceil(n/3)
    #print(nslide)
    #params = {'nslide':nslide , 'product':products,'range':range(1,nslide)}
    #allProds = [[products,nslide,range(1,nslide)],[products,nslide,range(1,nslide)]]

    allProds=[]
    catProd = Product.objects.values('category','id')
    #print(catProd)
    cats = {item['category'] for item in catProd}
    #print(cats)

    for cat in cats:
       prod = Product.objects.filter(category=cat)
       n = len(prod)
       nslide = ceil(n/3) 
       allProds.append([prod, range(1,nslide), nslide])
       #print(allProds)
    #params = {'allProds':allProds}
    return render(request,'shop/index.html',{'allProds':allProds})

    
'''def home(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        products = Product.objects.filter(category=cat)
        n = len(products)
        nSlides = n // 3 + ceil((n / 3) - (n // 3))
        allProds.append([products, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)'''

def about(request):
     return render(request,'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =  request.POST.get('email')
        phone = request.POST.get('phone')
        desc =  request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        
    return render(request,'shop/contact.html')

def search(request):
    query = request.GET.get('search')
    allProds=[]
    catProd = Product.objects.values('category','id')
    print(catProd)
    cats = {item['category'] for item in catProd}
    print(cats)
    for cat in cats:
       prodtemp = Product.objects.filter(category=cat)
       print(prodtemp)
       prod  = [item for item in prodtemp if searchMatch(query,item)]
       n = len(prod)
       nslide = ceil(n/3) 
       print(prod)
       if len(prod)!=0:
            allProds.append([prod, range(1,nslide), nslide])
    params = {'allProds':allProds,'msg':""}

    if len(allProds)==0:
       params = {'msg':"Please Make Sure To Enter Relevant Search Value"}
       print(params)
    return render(request,'shop/search.html',params)

def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category:
        return True
    else:
       return False
        


def track(request):
    if request.method == "POST":
        email = request.POST.get('email')
        orderId = request.POST.get('orderId')
        print("orderid",orderId)
        try:
            order = Order.objects.filter(order_Id=orderId,email=email)
            print(order)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_Id=orderId)
                print(update)
                updates = []
                for item in update:
                    print(update.update_desc)
                    print(update)
                    updates.append({'text':item.update_desc})
                    print(updates)
                    #response = json.dumps([updates,order[0].item_json],dfault=str)
                    #print(response)
                return HttpResponse("hiiiiiiiiii")
            else:
                return HttpResponse('else{}')
        except Exception:
            return HttpResponse('error{}')
    return render(request,'shop/tracker.html')


def check(request):
    if request.method == "POST":
        itemJson = request.POST.get('itemJson')
        name = request.POST.get('name')
        email = request.POST.get('email')
        Zip = request.POST.get('Zip')
        address = request.POST.get('address1')+" "+ request.POST.get('address2')
        city = request.POST.get('City')
        state = request.POST.get('State')
        phone = request.POST.get('Phone')
        order = Order(name=name, email=email,Zip=Zip,address=address,city=city,state=state,phone=phone,itemJson=itemJson)
        order.save()
        thank=True
        id=order.order_Id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')


def prodview(request,myid):
    product = Product.objects.filter(id=myid)

    return render(request,'shop/prodview.html',{'product':product[0]})


