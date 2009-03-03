from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    allow_comments = models.BooleanField()
    
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 255)
    entries = models.ManyToManyField(Entry)
    
    def __unicode__(self):
        return self.name
