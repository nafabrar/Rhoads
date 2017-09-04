from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Genre(models.Model):
    """Genre class"""


    genre=models.CharField(max_length=100)
class Album(Genre):
    """Album class"""
    artist1 = models.CharField(max_length =250)

    artist = models.CharField(max_length =250)
    album_title= models.CharField(max_length =500)
    # genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length= 1000)

    def get_absolute_url(self):
        return reverse ('music:detail',kwargs={'pk':self.pk})
    # returns the album details page

    def __str__(self):
        return self.album_title+ '-' + self.artist
"""Song Class"""
class Song(models.Model):
    owner = models.ForeignKey(User)
    song = models.FileField()
    song_title=models.CharField(max_length=250)
    album = models.ForeignKey(Album,on_delete = models.CASCADE)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title


class Blog(models.Model):
    """Topic/A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return self.text



class content(models.Model):
    pass
