from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'), 
    path("signup", views.handleSignup1, name='handleSignup'), 
    path("login", views.handleLogin, name='handleLogin'), 
    path("logout", views.handleLogout, name='handleLogout'), 
    path("DataScience", views.dataSci, name='dataScience'), 
    path("Python", views.pytho, name='python'), 
    path("WebDevelopment", views.WebDevelopment, name='webdevelopment'), 
]