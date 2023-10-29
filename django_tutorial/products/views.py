from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Offer,Offer2,new_user,Buy,new_user1,Buy2
from .forms import BookingForm
from hashlib import sha256
from django.contrib.auth.decorators import login_required


# Create your views here.

def dummy(request):
   

    

    users = new_user1.objects.all()  

    products  = Product.objects.all()
    # email=request.POST.get('email')
    # return render(request,'index1.html',{'products':products,'name':username,'email':email})
    return render(request,'home.html',{'products':products,'users':users,})
    #return HttpResponse("<h1>welcome to django project</h1>")

def register(request):
    
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
       
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        landmark=request.POST.get('landmark')

        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        password=sha256(pass2.encode()).hexdigest()
        new_user1(username=username,email=email,phone=phone,country=country,state=state,city=city,landmark=landmark ,password=password).save()
        if new_user1:
            user_details=new_user1.objects.get(username=username,password=password,email=email,phone=phone,country=country,state=state,city=city,landmark=landmark)
            id=user_details.id
            username_name=user_details.username
            email_name=user_details.email
            phone_name=user_details.phone
            country_name=user_details.country
            state_name=user_details.state
            city_name=user_details.city
            landmark_name=user_details.landmark



            request.session['id']=id
            request.session['username']=username_name
            request.session['email']=email_name
            request.session['phone']=phone_name
            request.session['country']=country_name
            request.session['state']=state_name
            request.session['city']=city_name
            request.session['landmark']=landmark_name

            
            return redirect('index')
        else:
            return redirect('reg')
        
    return render(request,'reg.html')


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        password2=sha256(password.encode()).hexdigest()
        user=new_user1.objects.filter(username=username,password=password2)
        if user:
            user_details=new_user1.objects.get(username=username,password=password2,)
            id=user_details.id
            username_name=user_details.username
            email_name=user_details.email
            phone_name=user_details.phone
            country_name=user_details.country
            state_name=user_details.state
            city_name=user_details.city
            landmark_name=user_details.landmark





            request.session['id']=id
            request.session['username']=username_name
            request.session['email']=email_name
            request.session['phone']=phone_name
            request.session['country']=country_name
            request.session['state']=state_name
            request.session['city']=city_name
            request.session['landmark']=landmark_name

            return redirect('index')
        else:
            return redirect('login')
    return render(request,'login.html')

def index(request):
    
    username=request.session['username']
    email=request.session['email']
    phone=request.session['phone']
    country=request.session['country']
    state=request.session['state']
    city=request.session['city']
    landmark=request.session['landmark']

    

    users = new_user1.objects.all()  

    products  = Product.objects.all()
    # email=request.POST.get('email')
    # return render(request,'index1.html',{'products':products,'name':username,'email':email})
    return render(request,'index1.html',{'products':products,'users':users,'name':username,'email':email,'phone':phone,'country':country,'state':state,'city':city,'landmark':landmark})
    #return HttpResponse("<h1>welcome to django project</h1>")

def about(request):
    if request.method == "POST":


        if request.method == 'POST':
         name=request.POST.get('name')
         price=request.POST.get('price')
         username=request.POST.get('username')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         country=request.POST.get('country')
         state=request.POST.get('state')
         city=request.POST.get('city')
         landmark=request.POST.get('landmark')
        Buy2(name=name,price=price,username=username,email=email,phone=phone,country=country,state=state,city=city,landmark=landmark).save()
        

     
        

        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    # dict_dept={
    #     # 'dept':new_user1.objects.all()
    #     'dept':new_user1.objects.all()
        
    # }
    username=request.session['username']
    name=request.POST.get('name')
   

    # email=request.session['email']
    
    

    


    return render(request,'conform.html',{'name':username,'product':name,})



   

def contact(request):
    

   

        
    if request.method == 'POST':
        
        name=request.POST.get('name')
        price=request.POST.get('price')
        username=request.POST.get('username')
        Buy2(name=name,price=price,username=username).save()
     

    dict_dept={
        'dept':Product.objects.all()
    }
    return render(request,'index3.html',dict_dept)
   

    # return render(request,'index3.html')
    # return HttpResponse("<h1>welcome to django project</h1>")

    
def connect():

    return render(request,'connect.html',dict_dept)

