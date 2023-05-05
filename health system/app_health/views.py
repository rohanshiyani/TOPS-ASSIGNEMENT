from django.shortcuts import render
from app_health.models import *
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

def home(request):
    return render(request,"index.html")

def register(request):
    if request.method=="POST":
        try:
            User.objects.get(username=request.POST['email'])
            return render(request,"register.html",{'msg':"User Already Exist"})
        except:
            if request.POST['pass'] == request.POST['cpass']:
                global votp
                votp=random.randint(100000,999999)
                subject = 'OTP VERIFICATION HEALTH SYSTEM'
                message = f'Hi THANKS FOR CHOOSING YOUR OTP IS {votp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                temp={
                    'fname':request.POST['fname'],
                    'uname':request.POST['email'],
                    'pass':make_password(request.POST['pass'])
                }
                return render(request,"otp.html")
            else:
                return render(request,"register.html",{'msg':"Password and Confirm Password Not match"})
    else:   
        return render(request,"register.html")

    
def otp(request):
        if request.method=="POST":
            if votp==int(request.POST['otp']):
                User.objects.create(
                    fullname=temp['fname'],
                    username=temp['uname'],
                    password=temp['pass']
                )
                return render(request,"index.html")
            else:
                return render(request,"otp.html",{'msg':'Invalid OTP'})
        else:
            return render(request,"otp.html")

def login(request):
    if request.method=="POST":
        try:
            user_data=User.objects.get(username=request.POST['email'])
            if check_password(request.POST['pass'],user_data.password):
                request.session['email']=request.POST['email']
                request.session['name']=user_data.fullname
                session_user_data=User.objects.get(username=request.session['email'])
                return render(request,"index.html",{"session_user_data":session_user_data})
            else:
                return render(request,"login.html",{'msg':'Invalid Password'})
        except:
            return render(request,"login.html",{'msg':'Your account is not Found Please Register'})
    else:
        return render(request,"login.html")
    
def profile(request):
    try:
        request.session['email']
        session_user_data=User.objects.get(username=request.session['email'])
        if request.method=="POST":
            user_data=User.objects.get(username=request.session['email'])
            if request.POST['pass']:
                if check_password(request.POST['opass'],user_data.password):
                    if request.POST['pass'] == request.POST['cpass']:
                        user_data=User.objects.get(username=request.session['email'])
                        user_data.fullname=request.POST['fname']
                        user_data.contact=request.POST['contact']
                        user_data.password=make_password(request.POST['pass'])
                        try:
                            request.FILES['propic']
                            user_data.profilepic=request.FILES['propic']
                            user_data.save()
                        except:    
                            user_data.save()
                        return render(request,"profile.html", {"user_data":user_data,
                        "msg":"profile updated successfully","session_user_data":session_user_data})
                    else:
                        user_data=User.objects.get(username=request.session['email'])
                        return render(request,"profile.html",{"user_data":user_data,
                        "msg":"profile updated successfully","session_user_data":session_user_data})
                else:
                    return render(request,"profile.html", {"user_data":user_data,
                    "msg":"old password not match","session_user_data":session_user_data})
                
            else:
                user_data=User.objects.get(username=request.session['email'])
                user_data.fullname=request.POST['fname']
                try:
                    request.FILES['propic']
                    user_data.profilepic=request.FILES['propic']
                    user_data.save()
                except:    
                    user_data.save()
                return render(request,"profile.html", {"user_data":user_data,
                "msg":"password and cpassword not match","session_user_data":session_user_data})
        else:
            user_data=User.objects.get(username=request.session['email'])
            return render(request,"profile.html", {"user_data":user_data,
            "session_user_data":session_user_data})  
    except:
        return render(request,"index.html")
    
def logout(request):
    try:
        request.session['email']
        del request.session['email']
        return render(request, "index.html")
    except:
        return render(request, "index.html")
          
def forgot_password(request):
    if request.method == "POST":
        try:
            user_data=User.objects.get(username=request.POST['email'])
            request.session['e_email'] = request.POST['email']
            global votp
            votp = random.randint(100000, 999999)
            subject = 'HEALTH SYSTEM OTP VERIFICATION MAIL'
            message = f'Your OTP IS {votp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail(subject, message, email_from, recipient_list)
            return render(request, "forgot_otp.html",)
        except:
            return render(request, "forgot_password.html", {"msg": "User Not Exist"})
    else:
        return render(request, "forgot_password.html")

def forgot_otp(request):

    if request.method == "POST":
        # print(type(votp), type(request.POST['otp']))
        if votp == int(request.POST['otp']):
            return render(request, "reset_password.html")
        else:
            return render(request, "forgot_otp.html", {'msg': "OTP INCORRECT"})
    else:
        return render(request, "forgot_otp.html")
    
def reset_password(request):
    if request.method == "POST":
        if request.POST['pass'] == request.POST['cpass']:
            user_data = User.objects.get(username=request.session['email'])
            user_data.password = make_password(request.POST['pass'])
            user_data.save()
            return render(request, "index.html", {'msg': "Password Reset Succesfully"})
        else:
            return render(request, "reset_password.html", {'msg': "Passwrod And confrim password not match"})
    else:
        return render(request, "reset_password.html")

def doctor(request):
    session_user_data=User.objects.get(username=request.session['email'])
    view_doctor=doctor_User.objects.all()
    return render(request,"doctor.html",{"view_doctor":view_doctor,"session_user_data":session_user_data})

def doctor_single(request,pk):
    session_user_data=User.objects.get(username=request.session['email'])
    view_doctorsingle=doctor_User.objects.get(id=pk)
    return render(request,"doctor_single.html",{"view_doctorsingle":view_doctorsingle,"session_user_data":session_user_data})
    


def disease(request):
    session_user_data=User.objects.get(username=request.session['email'])
    view_disease=disease_User.objects.all()
    return render(request,"disease.html",{"view_disease":view_disease,"session_user_data":session_user_data})
    
def disease_single(request,pk):
    session_user_data=User.objects.get(username=request.session['email'])
    view_diseasesingle=disease_User.objects.get(id=pk)
    return render(request,"disease_single.html",{"view_diseasesingle":view_diseasesingle,"session_user_data":session_user_data})
    
def medicine(request):
    session_user_data=User.objects.get(username=request.session['email'])
    view_medicine=medicine_User.objects.all()
    return render(request,"disease.html",{"view_medicine":view_medicine,"session_user_data":session_user_data})
    
def medicine_single(request,pk):
    session_user_data=User.objects.get(username=request.session['email'])
    view_diseasesingle=medicine_User.objects.get(id=pk)
    return render(request,"medicine_single.html",{"view_medicinesingle":view_medicinesingle,"session_user_data":session_user_data})
    
