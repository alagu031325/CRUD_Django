from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label='Date of Birth',
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy'})
    )
    
    class Meta:
        model = Person
        fields = ['first_name','last_name','age','email_id','phone_number','date_of_birth','username','password']


# - Update a record

class UpdateRecordForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        label='Date of Birth',
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy'})
    )

    class Meta:

        model = Person
        fields = ['first_name','last_name','age','email_id','phone_number','date_of_birth','username','password']