from django.shortcuts import render
from rest_framework import viewsets
from profiles_api import models,serializers
# Create your views here.
class APIViewSet(viewsets.ModelViewSet):
    """One To Many Example"""
    serializer_class = serializers.AlbumSerializer
    queryset = models.Album.objects.all()
    #http_method_names allows only defined http method
    http_method_names = ['get','post','put']