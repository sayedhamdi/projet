from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render ,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm,CondidatureForm
from .models import CustomUser,Condidature
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return render(request,"JetPlateform/SignIn.html")
    return render(request,"JetPlateform/Home.html",{"user":request.user.username})

def signIn(request):
    #if logged in redirect to home
    if request.method =="POST":
        email = request.POST.get('email')
        username = CustomUser.objects.get(email=email).username
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request,"JetPlateform/SignIn.html")
    return render(request,"JetPlateform/SignIn.html")

def signUp(request):
    #if logged in redirect to home
    form = CustomUserCreationForm()
    if request.method == "POST":
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            print(request.POST)
            f.save()
            return redirect(reverse('home'))
    return render(request,"JetPlateform/SignUp.html",{"form":form})

def logout(request):
    #redirect to home or login
    logout(request)
    return render(request,"JetPlateform/SignIn.html")
    #return render(reverse(home))
    pass

def userProfile(request):
    #if not logged in return to login
    return render(request,"JetPlateform/UserProfile.html")

def infoSession(request):
    #if not logged in return to login
    return render(request,"JetPlateform/InfoSession.html")

def condidature(request):
    #if not logged in return to login
    if not request.user.is_authenticated:
        context = {"message":"You are not logged in "}
        return render(request,"JetPlateform/SignIn.html",context)
    else:
        user = request.user
        condidature = Condidature.objects.get(user=user)
        if condidature is not None:
            context = {"condidature":condidature}
            return render(request,"JetPlateform/Condidature.html",context)
        form = CondidatureForm()
        context = {"form":form}
        if request.method == "POST":
            f = CondidatureForm(request.POST)
            if f.is_valid():
                print(request.POST)
                f.save()
                return redirect(reverse('home'))
        return render(request,"JetPlateform/Condidature.html",context)
