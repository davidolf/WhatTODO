'''
Created on Aug 14, 2014

@author: david
'''

from rest_framework import generics, permissions

from .serializers import TagSerializer, TodoSerializer
from WhatTODO.models import Tag, Todo

class TagList(generics.ListCreateAPIView):
    model = Tag
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
    
class TagDetail(generics.RetrieveAPIView):
    model = Tag
    serializer_class = TagSerializer
    lookup_field = 'text'
    
class TodoList(generics.ListCreateAPIView):
    model = Todo
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]
    
class TodoDetail(generics.RetrieveAPIView):
    model = Todo
    serializer_class = TodoSerializer