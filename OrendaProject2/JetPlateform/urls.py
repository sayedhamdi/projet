from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signIn,name="signIn"),
    path("signup",views.signUp,name="signUp"),
    path("logout",views.signIn,name="logout"),
    path("userProfile",views.userProfile,name="userProfile"),
    path("condidature",views.condidature,name="condidature"),
    path("infoSession",views.infoSession,name="infoSession"),
]
