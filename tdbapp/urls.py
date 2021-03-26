from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name='contact'),
    path('automobile', views.automobile, name='automobile'),
    path('healthcare', views.healthcare, name='healthcare'),
    path('retail', views.retail, name='retail'),
    path('construction', views.construction, name='construction'),
    path('smartcity', views.smartcity, name='smartcity'),
    path('upai', views.upai, name='upai'),
    path('fds', views.fds, name='fds'),
    path('fads', views.fads, name='fads'),
    path('ddds', views.ddds, name='ddds'),
    path('tds', views.tds, name='tds'),
    path('about', views.about, name='about'),
    path('leads', views.leads, name="leads")
    

]