from django.contrib import admin
from django.urls import path,include
from .import views,auth
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('course', views.course, name='course'),
    path('contact-us', views.contact, name='contact'),
    path('about-us', views.about, name='about'),
    
    path('auth/login',auth.login,name='login'),
    path('auth/register',auth.register,name='register'),
]
