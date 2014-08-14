'''
Created on Aug 14, 2014

@author: david
'''
from rest_framework import serializers

from WhatTODO.models import Todo, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('text',)

class TodoSerializer(serializers.ModelSerializer):
    tag = TagSerializer(required=False)
    
    class Meta:
        model = Todo
        fields = ('tag','text', 'due',)