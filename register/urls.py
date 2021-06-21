from django.urls import path, re_path
from register.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.auth import logout

urlpatterns = [
    path('signup/seller', signup_seller, name="signup"),
    path('signup/user', signup_user),
    path('login/', auth_views.LoginView.as_view(template_name = "login/login.html"), name = "login"),
    url(r'^logout/$', log_out, name='logout'),
]
