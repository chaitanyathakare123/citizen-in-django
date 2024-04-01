
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("track",views.track,name='track'),
    path("contact",views.contact,name='contact'),
    path("login",views.login,name='login'),
    path('register/', views.register, name='register'),
    path("logout",views.logout,name='logout'),
<<<<<<< HEAD
    path("live",views.live,name='live'),
=======
    path("flags",views.flags, name='flags')
>>>>>>> 4ac008e64a23991f4185eb76288da702797bb5e2
]