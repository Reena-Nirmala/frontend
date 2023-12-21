from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'welcome.html')

def login(request):
    return render(request,'login.html')

def summarize(request):
    return render(request,'summarize.html')

def registration(request):
    return render(request,'registration.html')
    

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def logout(request):
    return render(request,'welcome.html')
