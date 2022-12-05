from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    
    class Meta:
        # inherits from ShortURL model
        model=ShortURL

        #field that will receive the user's imput
        fields = {'original_url'}

        # to add the styling css
        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL here '})
        }