from django import forms
from shop.models import Ingredient


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'price', 'description', 'image', 'category', 'allergens')
