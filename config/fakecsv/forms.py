from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .buslogic import schema


class NewSchemaForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'name-input', 'placeholder':'Name'}))
    column_separator = forms.ChoiceField(choices=schema.COLUMNS)
    string_character = forms.ChoiceField(choices=schema.CHARACTERS)


class AddColumnForm(forms.Form):
    name_column = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'name-input', 'placeholder':'Name column'}))
    type = forms.ChoiceField(choices=schema.TYPES)
    from_int = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'from-int', 'initial': 0}))
    to_int = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'to-int', 'initial': 0}))
    order = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'order'}))

 
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Login",
        widget=forms.TextInput(attrs={
            'class': 'reg-input'
        })
        )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'reg-input'
        })
        )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'reg-input'
            })
        )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={
            'class': 'reg-input'
            })
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

