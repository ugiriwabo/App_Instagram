from django.db import models

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =30)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save() 