from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signIn,name="signIn"),
    #path("signup",views.signUp,name="signUp"),
    path("logout",views.logout_view,name="logout"),
    path("userProfile",views.userProfile,name="userProfile"),
    path("condidature",views.condidature,name="condidature"),
    path("infoSession",views.infoSession,name="infoSession"),
    path("signup",views.signUp,name="signUp"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
