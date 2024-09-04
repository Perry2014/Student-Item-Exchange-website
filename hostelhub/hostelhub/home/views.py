from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from django.conf import settings
import os
from .models import products
from accounts.models import profile

# Create your views here.

def home (request):
    items=products.objects.all()[:6]
    
    return render(request,"home.html",{'items':items})

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def homeafterlogin(request):
    items=products.objects.all()
    current_user=request.session['username']
    user = profile.objects.filter(username=current_user).values()

    sellername=user[0]['name']
    print(sellername)
    
    return render(request,"homeafterlogin.html",{'items':items,'name':sellername})

def product(request,item_id):
    item=products.objects.get(id=item_id)
    return render(request,"product.html",{'item':item})

def profile1(request):
    current_user=request.session['username']
    user = profile.objects.filter(username=current_user).values()

    sellername=user[0]['name']
    username=user[0]['username']
    items=products.objects.filter(sellername=current_user)
    return render(request,"profile1.html",{'items':items,'name':sellername})

    

def additem(request):
    if request.method =='POST' and request.FILES['image']:
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        # image = request.POST['image']
        image=request.FILES['image']
        fs = FileSystemStorage()
        filename=fs.save(image.name,image)
        url = fs.url(filename)
        image=url
        # image_path = os.path.join(settings.MEDIA_ROOT, 'pics', image.name)
        # with open(image_path, 'wb+') as destination:
        #         for chunk in image.chunks():
        #             destination.write(chunk)
        # if 'image' in request.FILES:
        #     image = request.FILES['image']
        #     # Specify the directory where you want to save the image
        #     image_path = os.path.join(settings.MEDIA_ROOT, 'pics', image.name)
        #     with open(image_path, 'wb+') as destination:
        #         for chunk in image.chunks():
        #             destination.write(chunk)
        # else:
        #     # Handle the case where no file is uploaded
        #     image_path = None
        # if 'image' in request.FILES:
        #     image = request.FILES['image']
        # else:
        #     # Handle the case where no file is uploaded
        #     image = None

        # user = profile.objects.filter(username=username).values()
        current_user=request.session['username']
        user = profile.objects.filter(username=current_user).values()

        sellername=user[0]['username']
        sellermobileNum=user[0]['mobile_number']

        product1 = products.objects.create(name=name,description=description,price=price,image=image,sellername=sellername,sellermobileNum=sellermobileNum)
        product1.save()
        # product2=products.objects.filter(name=name,sellername=sellername)
        # product2.delete()
        # print('product added')
        return redirect('profile1')


    return render(request,"additem.html")


def deleteitem(request):
    if request.method =='POST':
        id=request.POST['id']
        name=request.POST['name']
        current_user=request.session['username']
        user = profile.objects.filter(username=current_user).values()
        sellername=user[0]['username']
        product2=products.objects.filter(id=id,name=name,sellername=sellername)
        product2.delete()
        return redirect('profile1')


    return render(request,"deleteitem.html")