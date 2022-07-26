
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

from eapp.models import category, product,cart
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

#ADMIN PAGE
def adminhome(request):
    return render(request,'admin-home.html')  

def addproduct(request):
    cors=category.objects.all()
    context={'cors':cors}
    return render(request,'addproduct.html',context)

def viewproduct(request):
    pro=product.objects.all()
    return render(request,'viewproduct.html',{'pro':pro})   

def cate(request):
    return render(request,'adcategory.html')

def viewusers(request):
    std=User.objects.filter(is_superuser=0)
    return render(request,'admin-viewuser.html',{'std':std})


#USER PAGE 
def userhome(request):
    pro=product.objects.all()
    return render(request,'user-home.html',{'pro':pro}) 
   
        
         


def usercreate(request):
    if request.method=='POST':
        name=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already exists!!!...')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                     first_name=name,
                     last_name=lname,
                     username=username,
                     email=email,
                     password=password)
                user.save()
                messages.info(request,'successfully created')
        else:
             messages.info(request,'password does not match!!!....')   
             return redirect('signup') 
        return redirect('signup')                
    else:
        return render(request,'signup.html')

# def loginuser(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         #request.session['uid']=user.id
#         if user is not None:
#             if user.is_staff:
#                 login(request)
#                 return render(request,'admin-home.html')   
#             else:
#                 auth.login(request,user)
#                 messages.info(request,f'welcome {username}')   
#                 return render(request,'user-home.html',{'std':user})

#         else:
#             messages.info(request,'invalid username and password invalid')   
#             return redirect('login')       
#     else:
#         return render(request,'login.html') 

# def login_user(request):
#     if request.method=='POST':
#         std=product.objects.all()
#         usern=request.POST['uname']
#         passw=request.POST['pass']
#         user=auth.authenticate(username=usern,password=passw)
#         if user is not None:
#             if user.is_staff:
#                 auth.login(request,user)
#                 return render(request,'admin-home.html')
#             else:
#                 login(request,user)
#                 messages.info(request,f'welcome {usern}')
#                 return render(request,'user-home.html',{'std':std, 'user':user})  
#         else:
#             messages.info(request,'Invalid username and password!!!!!')   
#             return redirect('login')    
#     else:
#         return render(request,'login.html')           


def login_user(request):
    
    if request.method=='POST':

        pro=product.objects.all()
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
         # request.session["uid"]=user.id
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return render(request,'admin-home.html')
            else:
                # login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return render(request,'user-home.html',{'pro':pro, 'user':user})
                # return redirect('userhomepage')
        else:
            messages.info(request,'Invalid username and password')
            return redirect('login')
    else:
         return render(request,'login.html')
            





def products_add(request):
    if request.method=='POST':
        name=request.POST['product_name']
        descr=request.POST['description']
        price=request.POST['price']
        sel=request.POST['sel']
        cat=category.objects.get(id=sel)
        #image=request.FILES.get('file')
        if request.FILES.get('file')is not None:
            image = request.FILES.get('file')
        else:
            image = "static/image/default.jpg"

        pro=product(product_name=name,descrption=descr,price=price,image=image,category=cat)
        pro.save()
        messages.info(request,'product add suceessfully')
        return redirect('addproduct')
    return render(request,'addproduct.html')    



def addcate(request):
    if request.method=='POST':
        name=request.POST['category_name'] 
        cat=category(category_name=name)
        cat.save()
        messages.info(request,'category add successfully') 
        return redirect('cate')
    return render(request,'adcategory.html')

def delete(request,pk):
    std=product.objects.get(id=pk)  
    std.delete()
    return redirect('viewproduct')

def deleteuser(request,pk):
    std=User.objects.get(id=pk) 
    std.delete()
    return redirect('viewusers')   


def cartitem(request,pk,k):
    prod=product(id=pk)
    user1=User(id=k)
    t=cart(product=prod,
          User=user1)
    t.save()
    return redirect('userhome')



def details(request,pk,k):
    pro=product.objects.get(id=pk)
    return render(request,'viewdetails.html',{'pro':pro, 'u':k})

def viewcart(request,pk):
    ca=cart.objects.filter(User=pk) 
    return render(request,'cart.html',{'cart':ca})   

def deletecart(request,pk):
    ca=cart.objects.get(id=pk)
    ca.delete()
    #return redirect('viewcart')
    return render(request,'cart.html')

def myprofile(request,pk):
    std=User.objects.get(id=pk)
    return render(request,'profile.html',{'std':std})   

def listcart(request):
    ca=cart.objects.all()
    return render(request,'cartitems.html',{'item':ca})  

def deleteitem(request,pk):
    item=cart.objects.get(id=pk)
    item.delete()
    return redirect('listcart')  

def editproduct(request,pk):
    pro=product.objects.get(id=pk)
    ca=cart.objects.all()
    if request.method=='POST':
        pro.product_name=request.POST['product_name']
        pro.descrption=request.POST['descrption'] 
        pro.price=request.POST['price']
        pro.image=request.FILES('file')  
        c=request.POST['sel']
        pro.category=category.objects.get(id=c) 
        pro.save()     
        return redirect('viewproduct')
    return render(request,'editproduct.html',{'pro':pro , 'ca':ca})    