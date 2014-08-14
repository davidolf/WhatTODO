'''
Created on Aug 12, 2014

@author: david
'''
from WhatTODO import models
from django.contrib import admin

admin.site.register(models.Tag)
admin.site.register(models.Todo)