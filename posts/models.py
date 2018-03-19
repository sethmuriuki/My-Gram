from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)

    def save_profile(self):
        self.save()
        
    def __str__(self):
        return self.user.username


def Create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(Create_profile, sender=User)


class Images(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True)
    name = models.CharField(max_length=30)
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, null=True)    
    
    class Meta:
       ordering = ['-date_uploaded']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_user(cls, search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images

    @classmethod
    def get_image_by_id(cls, image_id):
        images = cls.objects.get(id=image_id)
        return images

class Comments(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True)
    image = models.ForeignKey(Images, null=True)
    time_comment = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
       ordering = ['-time_comment']



