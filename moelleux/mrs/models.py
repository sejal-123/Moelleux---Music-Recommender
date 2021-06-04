from django.db import models
from django.contrib.auth.models import User

class SearchModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    song_name=models.CharField(max_length=100, null=True, blank=True)
    song_artist=models.CharField(max_length=100, null=True, blank=True)

class FeedbackModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    rating = models.FloatField()
    feedback = models.TextField()
    
