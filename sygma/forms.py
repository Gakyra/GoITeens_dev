from django import forms
from .models import Stuff

class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['stuff_id', 'stuff_name', 'stuff_desc', 'photo', 'price']
