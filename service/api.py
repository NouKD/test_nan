from . import models
from rest_framework import viewsets
from . import serializers
from rest_framework import generics
from django_filters import rest_framework as filters

class CategorieArticleViewSet (viewsets.ModelViewSet):
    queryset = models.CategorieArticle.objects.filter(status=True)
    serializer_class = serializers.CategorieArticleSerializer
    filter_fields = ('nom',)

class TagViewSet (viewsets.ModelViewSet):
    queryset = models.Tag.objects.filter(status=True)
    serializer_class = serializers.TagSerializer
    filter_fields = ('nom',)


class ArticleViewSet (viewsets.ModelViewSet):
    queryset = models.Article.objects.filter(status=True)
    serializer_class = serializers.ArticleSerializer
    filter_fields = ('titre', 'categorie', 'auteur',)


class CommentaireViewSet (viewsets.ModelViewSet):
    queryset = models.Commentaire.objects.filter(status=True)
    serializer_class = serializers.CommentaireSerializer
    filter_fields = ('nom',)