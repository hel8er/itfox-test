from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import News
from .serializers import NewsSerializer


class NewsAPIView(generics.ListAPIView):
    """Вью получения списка новостей"""

    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication]
    queryset = News.objects.all()
    http_method_names = ['get']

    def list(self, request):

        serializer = NewsSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
