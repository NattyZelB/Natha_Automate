from django import forms
from .models import CompressionImage

class CompressImageForm(forms.ModelForm):
    class Meta:
        model = CompressionImage
        fields = ('original_img', 'quality')

    original_img = forms.ImageField(label='Upload an Image')
