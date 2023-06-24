from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','author','body','created_at')
        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title tag'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Write somthing about..'}),
            'created_at':forms.DateTimeInput(attrs={'class':'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','body')
        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title tag'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Write somthing about..'}),
        }