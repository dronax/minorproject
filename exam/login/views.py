from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from exam import settings
from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .models import *

from login.models import QuesModel
from . tokens import generate_token
import re,random
regex = r'[a-z]+\.\d{3}bct\d{3}@acem\.edu\.np'



# Create your views here.
def home(request):
    return render(request,"login/index.html")

def signup(request):

    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        dob =request.POST['dob']
        pass1 = request.POST['pass1']
        pass2 =request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,'Username Already Exists! Please try other Usernames')
            return redirect('signup')
        if re.fullmatch(regex,email) == None:
               messages.info(request,"Only ACEM bct students are accepted.")
               return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request,'Email already Registerd!')
            return redirect('signup')

        if len(username)>20:
            messages.error(request,'Username Must be under 15 Chaaracters')
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request,"Password Didn't Match") 
            return redirect('signup')


        if not username.isalnum():
            messages.error(request,'Username Must Be Alpha-Numeric')
            return redirect('signup')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.middle_name =mname
        myuser.last_name =lname
        myuser.date_of_birth =dob 
        myuser.is_active =False
        myuser.save()

        messages.success(request,"Your Account Has Been Successfully Created. We have Sent you a Confirmation Email,Please Confirm your email in order to activate your account")

        #Welcome Email
        subject="Welcome To Assesment Evaluation System- Admin"
        message ="Hello"+ myuser.first_name+"!!\n"+"Welcome To Assesment Evaluation System Website\n We have sent you a confirmation email,please confirm your Email adddress in order to activate your Account.\n\n Thanking You"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]

        #Email  Address Confirmation Email
        current_site=get_current_site(request)
        email_subject = "Confirm  your email @ Assesment Evaluation System Login!!"
        message_2 = render_to_string('email_confirmation.html',{
            'name':myuser.first_name,
            'domain': current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser),
            'code' :random.randint(100000,999999)
        })
        email =EmailMessage(
            email_subject,
            message_2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently=True
        email.send()

        send_mail(subject, message,from_email,to_list,fail_silently=True )
        

        return redirect('signin')
    return render(request,"login/signup.html")

def signin(request):

    if request.method=='POST':
        username = request.POST['username']
        pass1 =request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname= user.first_name
            return render (request,"login/loginhome.html",{'fname':fname})


        else:
            messages.error(request,"Bad Credentials")
            return redirect('signin')
    return render(request,"login/signin.html")

def signout(request):
   logout(request)
   messages.success(request,"Logged out Successfully!")
   return redirect('home')

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active =True
        myuser.save()
        login(request,myuser)
        return redirect('home')
    else:
        return render (request,'activation-failed.html')


def signinas(request):
    return render(request,'login/signinas.html')

def about(request):
    return render(request,'login/about.html')

def takeexam(request):
    if request.method=='POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans==request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        context={
            'score':score,
            'time':request.post.get('timer'),
            'correct':correct,
            'wrong':'wrong',
            'total':'total'
        }
        return render(request,'login/takeexam.html',context)
    else:
        questions=QuesModel.objects.all()
        context={
            'questions':questions
        }
        return render(request,'login/takeexam.html',context)

def ability(request):
    ()

