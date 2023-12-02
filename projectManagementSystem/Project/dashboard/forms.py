from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from accounts.models import CustomUser


class ChangingPassword(PasswordChangeForm):
     old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

     class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')


class EditProfileForm(UserChangeForm):
    email = None
    password = None
    first_name = forms.CharField(label='First name', max_length=30, widget=forms.TextInput)
    contact = forms.CharField(label='contact', widget=forms.TextInput, max_length=15)
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'contact')