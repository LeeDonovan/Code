from django.http import JsonResponse
from django.shortcuts import render

# third part imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


class PostView(mixins.ListModelMixin,
            mixins.CreateModelMixin,
            generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list( request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()