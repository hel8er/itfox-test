from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.Serializer):
    """Serializer for news model"""
    title = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=999999)
    pub_date = serializers.DateField()

    class Meta:
        model = News
