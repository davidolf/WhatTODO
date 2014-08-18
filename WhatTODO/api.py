'''
Created on Aug 14, 2014

@author: david
'''

from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from WhatTODO.models import Tag, Todo

from .serializers import TagSerializer, TodoSerializer

class TagList(generics.ListCreateAPIView):
    model = Tag
    serializer_class = TagSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

class TagDetail(generics.RetrieveAPIView):
    model = Tag
    serializer_class = TagSerializer
    lookup_field = 'text'
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    
class TodoList(generics.ListCreateAPIView):
    model = Todo
    serializer_class = TodoSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    
class TodoDetail(generics.RetrieveAPIView):
    model = Todo
    serializer_class = TodoSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)