from django.db import models

# Create your models here.
class Image(models:Model):
    location = models.CharField(max_length = 60)
    picture = models.ImageField(upload_to = 'images/', blank=True)
    caption = model.TextField(blank=True)


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
