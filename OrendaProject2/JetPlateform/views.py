from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render ,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .forms import CustomUserCreationForm,CondidatureForm
from .models import CustomUser,Condidature
from django.core.files.storage import FileSystemStorage
#test
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        print('not logged in ')
        return render(request,"JetPlateform/Home.html",{"user":request.user})
    return render(request,"JetPlateform/Home.html",{"user":request.user})


def signIn(request):
    #if logged in redirect to home
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
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


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

#signup with email
def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Jet account.'
            message = render_to_string('JetPlateform/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = CustomUserCreationForm()
    return render(request, 'JetPlateform/SignUp.html', {'form': form})




'''
def signUp(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    #if logged in redirect to home
    form = CustomUserCreationForm()
    if request.method == "POST":
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            print(request.POST)
            f.save()
            return redirect(reverse('home'))
    return render(request,"JetPlateform/SignUp.html",{"form":form})
'''

def logout_view(request):
    #redirect to home or login
    logout(request)
    return HttpResponseRedirect(reverse("signIn"))
    #return render(reverse(home))


def userProfile(request):
    #if not logged in return to login
    if not request.user.is_authenticated:
        context = {"message":"You are not logged in "}
        return render(request,"JetPlateform/SignIn.html",context)

    return render(request,"JetPlateform/UserProfile.html")

def infoSession(request):
    if not request.user.is_authenticated:
        context = {"message":"You are not logged in "}
        return render(request,"JetPlateform/SignIn.html",context)
    #if not logged in return to login
    return render(request,"JetPlateform/InfoSession.html")

def condidature(request):
    #if not logged in return to login
    if not request.user.is_authenticated:
        context = {"message":"You are not logged in "}
        return render(request,"JetPlateform/SignIn.html",context)
    else:
        condidature = request.user.condidatures.all()
        print(condidature)
        if condidature:
            context = {"condidature":condidature}
            return render(request,"JetPlateform/Condidature.html",context)
        form = CondidatureForm()
        context = {"form":form}
        if request.method == "POST":
            print(request.POST)
            cForm = request.POST
            etab = cForm['etablissement']
            print(request.FILES)
            fichiers =request.FILES.get('fichiers')
            fs = FileSystemStorage()
            fs.save(fichiers.name,fichiers)
            c = Condidature(etablissement=etab,fichiers=fichiers,isAccepted=False)
            c.save()
            request.user.condidatures.add(c)
            print(c)
            return redirect(reverse('home'))
        return render(request,"JetPlateform/Condidature.html",context)
