from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

USER = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = USER
        fields = ('username', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'role', 'name',
                  'contact_details', 'photo')
