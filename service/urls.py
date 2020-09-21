from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers
from . import api

router = routers .DefaultRouter()
router.register('categories',api.CategorieArticleViewSet)
router.register('tags',api.TagViewSet)
router.register('articles',api.ArticleViewSet)
router.register('commentaires',api.CommentaireViewSet)

urlpatterns = [
    path('', views.fashion, name='fashion'),
    path('single', views.single, name='single'),
    path('travel', views.travel, name='travel'),
    path('api/', include(router.urls)),
]