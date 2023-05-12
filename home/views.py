from multiprocessing import context
from turtle import home
from unittest import result
from django.shortcuts import render, redirect
from .models import datascience,Contact, webdev, python
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        value = {
            'name': name,
            'email':email,
            'content':content
        }
        error_msg=None
        if not name:
            error_msg = "First Name Required"
        elif len(name)<3:
            error_msg="First Name Must be 4 char long or more"
        elif(not email):
            error_msg = "Email Required"
        elif len(email)<4: 
            error_msg="Email Must be 4 char long or more"
        elif(not content):
            error_msg = "Write Some Query"
        elif len(content)<4: 
            error_msg="Write Some Query Correctly"
        if not error_msg:
            Cp=Contact(name=name, email=email, content=content)
            Cp.save()
            messages.success(request, "Your Query has been sent")
            return redirect('/')
        else:
            data ={
                'error': error_msg,
                'values':value
            }
            return render(request, 'contact.html', data)

    return render(request, 'contact.html')
    

def handleSignup1(request):
        if request.method=="POST":
            name = request.POST['name']
            email = request.POST['email']
            passw = request.POST['passw']
            cpass = request.POST['cpass']
            if len(name)<2 or len(email)<3 or len(passw)<3 or len(cpass)<3:
                messages.warning(request, "Pleace fill the form correctly!")
            else:
                myuser=User.objects.create_user(name,email,passw)
                myuser.save()
                messages.success(request, "You Signin Successfully!")
            
        return redirect('/')
            
def handleLogin(request):
    if request.method=="POST":
        loginname = request.POST['loginname']
        loginpass = request.POST['loginpass']
        user=authenticate(username=loginname, password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.warning(request,"Invalid Credentials, Please try again")
            return redirect('home')
def handleLogout(request):
    
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')


def dataSci(request):
    if request.user.is_anonymous:
        messages.warning(request,"LogIn First")
        return redirect('home')
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        gender = request.POST['gender']
        #validation
        value = {
            'first_name':firstname,
            'last_name':lastname,
            'email':email,
            'phone':phone,
            'dob': dob,
            'gender': gender
        }
        error_msg=None
        if(not firstname):
            error_msg = "First Name Required"
        elif len(firstname)<4: #firstname!=numeric
            error_msg="First Name Must be 4 char long or more"
        elif(not lastname):
            error_msg = "Last Name Required"
        elif len(lastname)<4: #firstname!=numeric
            error_msg="Last Name Must be 4 char long or more"
        elif(not email):
            error_msg = "Email Required"
        elif len(email)<4: 
            error_msg="Email Must be 4 char long or more"
        elif(not phone):
            error_msg = "Phone Number Required"
        elif len(phone)<10: 
            error_msg="Phone Must be 10 char long or more"
        elif(not dob):
            error_msg = "Date of Birst Required"
        elif dob > "2005-1-1": 
            error_msg="Your Date of Birth must be greater than 01/Jan/2005"
        elif not gender:
            error_msg = "Gender Required"

        # saving
        if not error_msg:
            print(firstname, lastname, email, phone, gender)
            obj = datascience(firstname=firstname, lastname=lastname,email=email,phone=phone,dob=dob, gender=gender)
            obj.save()
            messages.success(request, "Submitted Successfully")
            return redirect('/')
        else:
            # messages.warning(request, error_msg)
            data ={
                'error': error_msg,
                'values':value
            }
            return render(request, 'dataScience.html', data)
    return render(request, 'dataScience.html')

def pytho(request):
    if request.user.is_anonymous:
        messages.warning(request,"LogIn First")
        return redirect('home')
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        gender = request.POST['gender']
        #validation
        value = {
            'first_name':firstname,
            'last_name':lastname,
            'email':email,
            'phone':phone,
            'dob': dob,
            'gender': gender
        }
        error_msg=None
        if(not firstname):
            error_msg = "First Name Required"
        elif len(firstname)<4: #firstname!=numeric
            error_msg="First Name Must be 4 char long or more"
        elif(not lastname):
            error_msg = "Last Name Required"
        elif len(lastname)<4: #firstname!=numeric
            error_msg="Last Name Must be 4 char long or more"
        elif(not email):
            error_msg = "Email Required"
        elif len(email)<4: 
            error_msg="Email Must be 4 char long or more"
        elif(not phone):
            error_msg = "Phone Number Required"
        elif len(phone)<10: 
            error_msg="Phone Must be 10 char long or more"
        elif(not dob):
            error_msg = "Date of Birst Required"
        elif dob > "2005-1-1": 
            error_msg="Your Date of Birth must be greater than 01/Jan/2005"
        elif not gender:
            error_msg = "Gender Required"

        # saving
        if not error_msg:
            print(firstname, lastname, email, phone, gender)
            obj = python(firstname=firstname, lastname=lastname,email=email,phone=phone,dob=dob, gender=gender)
            obj.save()
            messages.success(request, "Submitted Successfully")
            return redirect('/')
        else:
            # messages.warning(request, error_msg)
            data ={
                'error': error_msg,
                'values':value
            }
            return render(request, 'python.html', data)
    return render(request, 'python.html')

def WebDevelopment(request):
    if request.user.is_anonymous:
        messages.warning(request,"LogIn First")
        return redirect('home')
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        gender = request.POST['gender']
        #validation
        value = {
            'first_name':firstname,
            'last_name':lastname,
            'email':email,
            'phone':phone,
            'dob': dob,
            'gender': gender
        }
        error_msg=None
        if(not firstname):
            error_msg = "First Name Required"
        elif len(firstname)<4: #firstname!=numeric
            error_msg="First Name Must be 4 char long or more"
        elif(not lastname):
            error_msg = "Last Name Required"
        elif len(lastname)<4: #firstname!=numeric
            error_msg="Last Name Must be 4 char long or more"
        elif(not email):
            error_msg = "Email Required"
        elif len(email)<4: 
            error_msg="Email Must be 4 char long or more"
        elif(not phone):
            error_msg = "Phone Number Required"
        elif len(phone)<10: 
            error_msg="Phone Must be 10 char long or more"
        elif(not dob):
            error_msg = "Date of Birst Required"
        elif dob > "2005-1-1": 
            error_msg="Your Date of Birth must be greater than 01/Jan/2005"
        elif not gender:
            error_msg = "Gender Required"

        # saving
        if not error_msg:
            print(firstname, lastname, email, phone, gender)
            obj = webdev(firstname=firstname, lastname=lastname,email=email,phone=phone,dob=dob, gender=gender)
            obj.save()
            messages.success(request, "Submitted Successfully")
            return redirect('/')
        else:
            # messages.warning(request, error_msg)
            data ={
                'error': error_msg,
                'values':value
            }
            return render(request, 'WebDevelopment.html', data)
    return render(request, 'WebDevelopment.html')