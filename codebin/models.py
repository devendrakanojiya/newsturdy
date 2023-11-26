

# Create your models here.
#models 
from django.db import models

# Create your models here.
class Codebin(models.Model):
    
    # VISIBILITY_CHOICES = [
    #     ('public', 'public'),
    #     ('private', 'private'),
    # ]
    # id = models.IntegerField(primary_key= True) 
    pastetitle = models.CharField(max_length=200)
    pastecontent = models.CharField(max_length=200)
    sid = models.IntegerField()
    visibility = models.CharField(max_length=10, default='public')  #choices= VISIBILITY_CHOICES, 

# string function
    def __str__(self):
        return self.pastetitle

    # def __init__(self, pastetitle, pastecontent, sid):
    #     self.pastetitle = pastetitle
    #     self.pastecontent = pastecontent
    #     self.sid = sid 


