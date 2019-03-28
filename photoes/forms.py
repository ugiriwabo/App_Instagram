from django import forms
from .models import Profile,Image

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['name','post_date','likes']
