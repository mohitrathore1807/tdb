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
    path('upai', views.upai, name='upai'),
    path('fds', views.fds, name='fds'),
    path('fads', views.fads, name='fads'),
    path('ddds', views.ddds, name='ddds'),
    path('tds', views.tds, name='tds'),
    path('dr.ai', views.heartrate, name='dr.ai'),
    path('about', views.about, name='about'),
    path('leads', views.leads, name="leads"),
    path('blogs', views.blog, name="blogs"),
    path('post/<str:id>',  views.post, name="post"),
    path('sitemap.xml',  views.sitemap, name="sitemap"),
    path('robots.txt',  views.robots, name="robots")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)