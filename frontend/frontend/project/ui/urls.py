from django import views
from django.urls import path
from . import views

app_name = 'ui'
urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration'),
    path('login/summarize',views.summarize,name='summarize'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('login/summarize/welcome',views.home,name='home'),
    path('registration/login',views.login,name='login'),
    path('registration/summarize',views.summarize,name='summarize'),
    path('registration/welcome',views.home,name='home'),
    path('login/welcome',views.home,name="home"),
    path('login/registration',views.registration,name ="registration"),
    path('login/forgotpassword',views.forgotpassword,name='forgotpassword'),
    
]
