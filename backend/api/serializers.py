from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model =Article
        #fields=("title","slug","author","content","publish","status")
        #exclude=("created","updated")
        fields="__all__"

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields="__all__"
