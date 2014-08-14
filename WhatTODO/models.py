'''
Created on Aug 11, 2014

@author: david
'''
from django.db import models

#class User(models.Model):
#    username = models.CharField(max_length=100)
#    firstname = models.CharField(max_length=100)
#    surname = models.CharField(max_length=100)
    
#    def __str__(self):
#        return self.username
    
class Tag(models.Model):
    text = models.CharField(max_length=100)
    
    def __str_(self):
        return self.text

class Todo(models.Model):
    text = models.CharField(max_length=1000)
#    owner = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    due = models.DateField()

    def __str__(self):
        return self.text