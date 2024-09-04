from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import profile,students
from home.models import products

# Create your views here.

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        mobile_number= request.POST['mobile_number']
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        student = students.objects.filter(email=email).values()
        if (student):
            emailuser =profile.objects.filter(email=email).values()
            if emailuser:
                print('email already taken')
                message='email already taken'
                
            else:
                user = profile.objects.filter(username=username).values()
                if user:
                    print('username already taken')
                    message='username already taken'
                    
                else:
                    if password == repassword:
                        profile1 = profile.objects.create(username=username,password=password,email=email,name=name,mobile_number=mobile_number)
                        profile1.save()
                        # print('user created')
                        return redirect('login')
                    else:
                        print('incorrect match of password')
                        message='incorrect match of password'
                
                
        else:
            print('you are not a student of NITAP')
            message='you are not a student of NITAP'
        return render(request,'signup.html',{'message':message})
        
    else:
        return render(request,'signup.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password']
        # user = profile.objects.get_by_natural_key(username)
        # user=profile.objects.get(username=username)
        user = profile.objects.filter(username=username).values()
        if (user and user[0]['password']==password1 ):
            request.session['username']=username

            return redirect('homeafterlogin')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')
    

def homeafterlogin(request):
    items=products.objects.all()
    current_user=request.session['username']
    user = profile.objects.filter(username=current_user).values()

    sellername=user[0]['name']
    print(sellername)
    
    return render(request,"homeafterlogin.html",{'items':items,'name':sellername})

def product(request,product_id):
    product=products.objects.get(pk=product_id)
    return render(request,"product.html",{'product':product})