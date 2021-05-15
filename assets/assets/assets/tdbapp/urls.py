from django.contrib import admin
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name='contact'),
    path('automobile', views.automobile, name='automobile'),
    path('healthcare', views.healthcare, name='healthcare'),
    path('retail', views.retail, name='retail'),
    path('construction', views.construction, name='construction'),
    path('smartcity', views.smartcity, name='smartcity'),
    path('about', views.about, name='about'),
    path('leads', views.leads, name="leads"),
    path('blogs', views.blog, name="blogs"),
    path('post/<id>',  views.post, name="post")
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)