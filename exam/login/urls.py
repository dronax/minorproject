from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path('signinas',views.signinas,name="signinas"),
    path('signup',views.signup,name="signup"),
    path('about',views.about,name="about"),
    path('signout',views.signout,name="signout"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    path('takeexam',views.takeexam,name='takeexam'),
]
