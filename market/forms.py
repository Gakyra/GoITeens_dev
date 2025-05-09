from django import forms
from .models import Bb
from django.forms import ModelForm, DecimalField
from django.forms.widgets import Select
from .models import GoITeen
from django.db import models
from django.contrib.auth.models import User
from .models import GoITeen, Rubric
from django.core import validators
from django.core.exceptions import ValidationError
from django import forms
from django.forms import modelformset_factory
from .models import ModelFormsetModel



class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'rubric']


class GoITeenForm(forms.ModelForm):
    price = forms.DecimalField(label='Price', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Rubric', help_text='Create it!',
                                    widget=forms.widgets.Select(attrs={'size': 8}))

    class Meta:
        model = GoITeen
        fields = ('title', 'content', 'price', 'rubric')
        labels = {'title': 'Name good'}


class GoITeenForm1(forms.ModelForm):
    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Last year snow':
            raise ValidationError("Can't sell")
        return val

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('Print desc')
        if self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError('Tell price')
        if errors:
            raise ValidationError(errors)

    title = forms.CharField(
        label='Name',
        validators=[
            validators.RegexValidator(regex='^A.{4,}$',
                                      message='So short')
            ]
    )





class ModelFormsetForm(forms.ModelForm):
    class Meta:
        model = ModelFormsetModel
        fields = ['name', 'email', 'department']

DjangoFormSet = modelformset_factory(
    ModelFormsetModel,
    form=ModelFormsetForm,
    extra=1,
    can_delete=True
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data

