from django import forms
from .models import Image, Comment


class WelcomeForm(forms.Form):
    your_name = forms.CharField(label = 'First Name',max_length = 30)
    email = forms.EmailField(label='Email')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['author']
