from django import forms
from .models import Profile,Image,Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date','likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']