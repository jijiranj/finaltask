from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .forms import RegistrationForm
from .models import Branches
from django.shortcuts import render, redirect

# Create your views here.
def demo(request):
    obj = Branches.objects.all()
    return render(request,"index.html",{'brnch':obj})

def login(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,password=password)

      if user is not None:
         auth.login(request,user)
         return redirect('/new')
      else:
          messages.info(request, "Invalid Credentials")
          return redirect('/login')
   return render(request,"login.html")



def detail(request,branch_id):
    branch=Branches.objects.get(id=branch_id)
    return render(request,"detail.html",{'branch':branch})




def register(request):
    if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password']
       cpassword = request.POST['password1']
       if password==cpassword :
          if User.objects.filter(username=username).exists():
             messages.info(request,"Username Taken")
             return redirect('/register')
          else:
              user = User.objects.create_user(username=username,password=password)
              user.save();
              return redirect('/login')

       else:
           messages.info(request,"password not matching")
           return redirect('/register')
    return render(request,"register.html")

# def formnew(request):
#     branch2 = Branches.objects.all()
#     return render(request,"formnew.html",{'branch2':branch2})


def logout(request):
    auth.logout(request)
    return redirect('/')

def new(request):
    return render(request,"new.html")



def user_registration(request):
    form_class = RegistrationForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
          user = form.save()
          login(request, user) # This will log the user in
          messages.info(request, "submitted successfully")
          return redirect('/login')
       else:
           form = RegistrationForm()
           messages.info(request,"Application Accepted")
    return render(request,'formnew.html',{'form': form})


def get_branches(request):
    district = request.GET.get('district')
    branches =[]
    if district == 'Calicut':
       branches = ['Kunnamkulam', 'Kodugallur', 'Wadakkanchery']
    elif district == 'Cochin':
        branches = ['Angamaly', 'Perumbavoor', 'Vytilla']
    elif district == 'Kollam':
        branches = ['Thenmala', 'Tirurkad', 'Paravoor']
    elif district == 'Kottayam':
        branches = ['Changanassery', 'Pala', 'Erattupetta']
    elif district == 'Malappuram':
        branches = ['Manjeri', 'Kottakkal', 'Tirur']
    elif district == 'Palakkad':
        branches = ['Chittur', 'Ottappalam', 'Kalpathy']
    data = {'branches': branches}
    return JsonResponse(data)













