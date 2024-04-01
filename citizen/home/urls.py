
from django.contrib import admin
from django.urls import path
from home import views
from .views import *
urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("track",views.track,name='track'),
    path("contact",views.contact,name='contact'),
    path("login",login_user,name='login'),
    path("register/", views.register_user, name='register'),
    path("logout",views.logout_user,name='logout'),
    path("flags",views.flags, name='flags')
]