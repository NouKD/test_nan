from rest_framework import serializers
from . import models

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsLetter
        fields = '__all__'        


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteInfo
        fields = '__all__'
        depth = 1        


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Presentation
        fields = '__all__'   
        depth = 1

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAccount
        fields = '__all__'
        depth = 1        


class OtherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherInfo
        fields = '__all__'   
        depth = 1        