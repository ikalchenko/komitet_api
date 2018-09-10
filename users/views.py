import django.contrib.auth.models as auth_models
from django.shortcuts import render
from rest_framework import generics, viewsets

from .serializers import TestSerializer

# Create your views here.


class TestViewSet(viewsets.ModelViewSet):
    model = auth_models.User
    queryset = auth_models.User.objects.all()
    serializer_class = TestSerializer


class SignUpView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
