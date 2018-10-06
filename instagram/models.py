from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Image(models.Model):
    location = models.CharField(max_length = 60)
    picture = models.ImageField(upload_to = 'images/', blank=True)
    caption = models.TextField(blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


    def save_image(self):
	    self.save()
    def update_image(self):
        self.update()
    def delete_image(self):
        self.delete()

    @classmethod
    def display_images(cls):
        images= cls.objects.all()
        return images


class Comment(models.Model):
    comment = models.CharField(max_length =60,blank=True)
    image = models.ForeignKey(Image, related_name = 'comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def save_comments(self):
        self.save()
    def update_comments(self):
        self.update()
    def delete_comments(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length =500, blank=True)
    user_pic = models.ImageField(upload_to = 'images/', blank=True)

    @classmethod
    def search_by_name(cls,search_term):
        profiles = cls.objects.get(name__icontains=search_term)
        return profiles

    @classmethod
    def get_profile(cls):
        profile=Profile.objects.all()
        return profile

    def __str__(self):
        return '{0}'.format(self.user.username)
