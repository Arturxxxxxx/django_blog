from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Post
from .serializers import PostSerializer, PostListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated 
from .permissions import IsOwnerOrReadOnly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['author']
    search_fields = ['title']
    # permission_classes = []

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]
        # return super().get_permissions()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class
    def get_serializer_context(self):
        return {'request':self.request}

