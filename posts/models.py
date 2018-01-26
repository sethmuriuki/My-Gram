from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ManyToManyField(categories)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()