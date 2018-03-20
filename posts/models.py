from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def find_profile(cls,name):
        found_profiles = cls.objects.filter(username__icontains = name).all()
        return found_profiles


        


def Create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(Create_profile, sender=User)


class Images(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True)
    name = models.CharField(max_length=30)
    caption = models.TextField()
    likes = models.PositiveIntegerField(default=0)
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



class Like(models.Model):
    '''
    Class defines the structure of a like on a an posted Image
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE, null= True)

    image = models.ForeignKey(Images,on_delete=models.CASCADE, null = True)

    def __int__(self):
        return self.user.username

    def save_like(self):
        self.save() 

    def unlike(self):
        self.delete()

    def like(self):
        self.likes_number = 2
        self.save()

    @classmethod
    def get_likes(cls,image_id):
        '''
        Function that get likes belonging to a paticular posts
        '''
        likes = cls.objects.filter(image = image_id)
        return likes 