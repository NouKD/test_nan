from . import models
from rest_framework import viewsets
from . import serializers
from rest_framework import generics
from django_filters import rest_framework as filters

class ContactViewSet (viewsets.ModelViewSet):
    queryset = models.Contact.objects.filter(status=True)
    serializer_class = serializers.ContactSerializer
    filter_fields = ('nom',)

class NewsLetterViewSet (viewsets.ModelViewSet):
    queryset = models.NewsLetter.objects.filter(status=True)
    serializer_class = serializers.NewsLetterSerializer
    filter_fields = ('email',)


class SiteInfoViewSet (viewsets.ModelViewSet):
    queryset = models.SiteInfo.objects.filter(status=True)
    serializer_class = serializers.SiteInfoSerializer
    filter_fields = ('email',)


class PresentationViewSet (viewsets.ModelViewSet):
    queryset = models.Presentation.objects.filter(status=True)
    serializer_class = serializers.PresentationSerializer
    filter_fields = ('nom',)

class UserAccountViewSet (viewsets.ModelViewSet):
    queryset = models.UserAccount.objects.filter(status=True)
    serializer_class = serializers.UserAccountSerializer
    filter_fields = ('user',)

class OtherInfoViewSet (viewsets.ModelViewSet):
    queryset = models.OtherInfo.objects.filter(status=True)
    serializer_class = serializers.OtherInfoSerializer
    filter_fields = ('addresse',)