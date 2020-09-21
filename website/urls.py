from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers
from . import api

router = routers .DefaultRouter()
router.register('contact',api.ContactViewSet)
router.register('news',api.NewsLetterViewSet)
router.register('info',api.SiteInfoViewSet)
router.register('presenation',api.PresentationViewSet)
router.register('user',api.UserAccountViewSet)
router.register('autre',api.OtherInfoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('connexion', views.connexion, name='connexion'),
    path('api/', include(router.urls)),
]