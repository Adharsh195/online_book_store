from django import forms
from . models import *

class Bookform(forms.Form):
    title=forms.CharField(max_length=200,label="Book Title")
    author=forms.CharField(max_length=100,label="Author Name")
    category=forms.CharField(max_length=50,label="Category Name")
    price=forms.DecimalField(max_digits=6,decimal_places=2,label="Price")
    description=forms.CharField(widget=forms.Textarea,label="Book Description")

class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name','cat_description']

        labels={
            'category_name':'category name',
            'cat_description':'description',
        }
        widget={
            'category_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter category name'}),
            'cat_descriptiion':forms.Textarea(attrs={'class':'form-control','placeholder':'enter category description'})
        }

        help_texts={
            'category_name':'enter a short and unique nmae for the category',
        }