from django import forms
from library.models import Category 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','type':"text" , 'placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','type':"text" , 'placeholder': 'Description'}),
                        
        }
