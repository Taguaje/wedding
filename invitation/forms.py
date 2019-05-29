from django import forms
from .models import Guest

class InvitationConfirm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('isComing', 'confirm')