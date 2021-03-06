from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =120)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save() 

    @classmethod
    def get_image(cls,id):
        Image.objects.all()

    @classmethod
    def search_user(cls,search_term):
        users=Image.objects.filter(name__icontains=search_term)
        return users

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length =30)
    profile_photo = models.ImageField(upload_to = 'pic/')
    bio=models.CharField(max_length =30)


    def save_profile(self):
        self.save() 
    
    @classmethod
    def get_profile(cls,id):
        Profile.objects.all()

    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()

class Comment(models.Model):  
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length =80)

    def save_comment(self):
        self.save() 

    @classmethod
    def get_comment(cls,id):
        Comments.objects.all()
    
    def __str__(self):
        return self.comment