from django import forms
from .models import Guest
from PIL import Image
import os


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Guest
        fields = ('avatar', 'x', 'y', 'width', 'height',)
        widgets = {
            'file': forms.FileInput(attrs={
                'accept': 'image/*'
            })
        }

    def save(self):

        guest = super(PhotoForm, self).save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(guest.avatar)
        cropped_image = image.crop((x, y, w + x, h + y))
        cropped_image.save(guest.avatar.path)

        return guest
