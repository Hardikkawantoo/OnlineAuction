
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from app1.models import items_data
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pytz import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#######################

# Create your views here.


def aboutus(request):
    
    return render(request,'aboutus.html')
def projects(request):
    return render(request,'projects.html')
def number(request):
    return render(request,'number.html')
def contact(request):
    if request.method == 'POST':
        form = Item_form(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Item_form()
    return render(request, 'contact.html', {'form' : form})
  
  
def success(request):
    return render(request, 'success.html')
  





    # context={'success':False}
    # if request.method=="POST":
    #     title= request.POST['ititle']
    #     cost_item=request.POST['icost']
    #     image=request.FILES['u_image']
    #     fs=FileSystemStorage()
    #     filename=fs.save(image.name, image)
    #     uploaded_file_url =fs.url(filename)
    #     print(title,cost_item,image)
    #     ins = items_data(i_name=title,cost=cost_item,upload=image)
    #     ins.save()
    #     context={'success':ins}
        

    # return render(request,'contact.html',context)
    
def index(request):
    if request.user.is_authenticated:
        cont=True
    else:
        cont=False
    alldata=items_data.objects.all()

    paginator=Paginator(alldata,1)
    page=request.GET.get('page')
    try:
        alldata=paginator.page(page)
    except PageNotAnInteger:
        alldata=paginator.page(1)
    except EmptyPage:
        alldata=paginator.page(paginator.num_pages)

    context={'ItemD':alldata,'Value':cont,'page':page}
    print(alldata)

    return render(request,'index.html',context)
    
# def login_user(request):
#     if request.method=="POST":

#         emailcheck=request.POST.get('email1')
#         passwordcheck=request.POST.get('password')

        

#         check1=Signup.objects.filter(email=emailcheck).exists()
#         check2=Signup.objects.filter(password1=passwordcheck).exists()

#         print(check1,check2)
#         print(emailcheck,passwordcheck)
#         if check1==True and check2==True:
            
#             return render(request,'choice.html')
    
#     return render(request,'login.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Choice')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Choice')
    context={}
    return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('loginPage')

def logout_view_home(request):
    logout(request)
    return redirect('index')

def Choice(request):
    if request.user.is_authenticated:
        return render(request,'choice.html',{})
    else:
        return render(request,'login.html')

def display_images(request):
  
    if request.method == 'GET':
  
        # getting all the objects of item images
        UImages = items_data.objects.all() 
        return render((request, 'contact.html',
                     {'item_images' : UImages}))

# def register(request):
#     if request.method =="POST":
#         form =UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f"New Account Created: {username}")
#             login(request,user)
#             messages.info(request,f"You are now logged in as {username}")
#             return redirect("index")
#         else:
#             for msg in form.error_messages:
#                 messages.error(request,f"{msg}: {form.error_messages[msg]}")
#     form=UserCreationForm
#     return render(request,"index.html", context={"form":form})


# def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("index")

# def login_request(request):
#     form = AuthenticationForm()
#     return render(request = request,
#                   template_name = "login.html",
#                   context={"form":form})

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request = request,
#                     template_name = "login.html",
#                     context={"form":form})

# def register(request):
#     if request.method=="POST":
#         first_name=request.POST.get('first_name')
#         last_name=request.POST.get('last_name')
#         email=request.POST.get('email')
#         password1=request.POST.get('password1') 
        
#         signup=Signup(first_name=first_name,last_name=last_name,email=email,password1=password1)
#         signup.save()

#         return render(request,'login.html')
        
#     return render(request,'register.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid form")
            user=form.cleaned_data.get('username')
            messages.success(request,'User '+user+' account has been successfully created')

            return redirect('loginPage')
        else:
            context={'form':form}
            return render(request,'register.html',context)

    else:
        context={'form':form}
        return render(request,'register.html',context)

def sellerPage(request):
    if request.user.is_authenticated:
        format = "%Y-%m-%d %I:%M:%S"
        now_utc = datetime.now(timezone('UTC'))
        now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
        Ctime = now_asia.strftime(format)
        alldata=items_data.objects.all()
        for x in alldata:
            print(type(x.timing))
        print(Ctime)
        context={'ItemD':alldata,'Ctime':Ctime}
    
        return render(request,'sellerPage.html',context)
    else:
        return render(request,'login.html')
    

def update(request, id):
    if request.user.is_authenticated:
        mymember = items_data.objects.get(id=id)
        template = loader.get_template('update.html')
        context = {
            'mymember': mymember,
                }
        return render(request,'update.html',context)
    else:
        return render(request,'login.html')
  

def updaterecord(request, id):
    if request.user.is_authenticated:
        cost = request.POST['cost']
        Top = request.user

  
        member = items_data.objects.get(id=id)
        member.Cost = cost
        member.Top_Bidder=str(Top)
        member.save()
        return redirect('sellerPage')
    else:
        return render(request,'login.html')
  