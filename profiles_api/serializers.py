from rest_framework import serializers
from profiles_api import models

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = ['order', 'title', 'duration']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = models.Album
        fields = ['album_name', 'artist', 'tracks']