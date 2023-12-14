from django.shortcuts import redirect,render

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'main/home.html')

def course(request):
    return render(request,'main/course.html')

def contact(request):
    return render(request,'main/contact-us.html')

def about(request):
    return render(request,'main/about-us.html')