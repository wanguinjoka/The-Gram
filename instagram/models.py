from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Image(models.Model):
    location = models.CharField(max_length = 60)
    picture = models.ImageField(upload_to = 'images/', blank=True)
    caption = models.TextField(blank=True)


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
    caption = models.TextField()
    image = models.ForeignKey(Image, related_name = 'comments', on_delete=models.CASCADE)

    def save_comments(self):
        self.save()
    def update_comments(self):
        self.update()
    def delete_comments(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length =500, blank=True)
    user_pic = models.ImageField(upload_to = 'images/', blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs)
         if created:
             Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.get(user__username__icontains=search_term)
        return profile
