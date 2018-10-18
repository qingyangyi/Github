"""为应用程序users定义URL模式"""
from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views

app_name='users'
urlpatterns=[
    #登录界面
    path('login/',LoginView.as_view(template_name='users/login.html'),
            name='login'),
    #注销
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register')
    ]
