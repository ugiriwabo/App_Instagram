# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver



# class Profile(models.Model):
#     photo=models.ImageField(upload_to='images/')
#     bio=models.TextField()
#     user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
#     follow=models.NullBooleanField(default=False)
    
#     def save_profile(self):
#         self.save()
#     def delete_profile(self):
#        self.delete()

#     def update_bio(self,bio):
#          self.bio=bio
#          self.save()

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

# class Image(models.Model):
#      name=models.CharField(max_length=100)
#      image=models.ImageField(upload_to = 'images/')
#      caption=HTMLField()
#      likes=models.IntegerField()
#      pub_date = models.DateTimeField(auto_now_add=True)
#      profile=models.ForeignKey(Profile, null=True)
#      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     
#      def save_image(self):
#          self.save()

#      def delete_image(self):
#        self.delete()
       
#      def update_caption(self,cap):
#          self.caption=cap
#          self.save()
   
    
# class Comment(models.Model):
#     comment=models.TextField()
#     image=models.ForeignKey(Image,default=0)
#     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     def save_comment(self):
#         self.save()
#     def delete_comment(self):
#        self.delete()

#     def update_comment(self,comment):
#          self.comment=comment
#          self.save()


# class Follow(models.Model):
#      follower=models.ForeignKey(Profile, related_name='follower')
#      following=models.ForeignKey(Profile ,related_name='followee')