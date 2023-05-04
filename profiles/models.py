from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default_profile_pic.jpg')
    interests = models.ManyToManyField('Interest', blank=True)

    def __str__(self):
        return self.user.username

class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
