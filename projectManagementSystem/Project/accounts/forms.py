from django import forms
from .models import owner,employee,manager,CustomUser
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models.fields import BLANK_CHOICE_DASH


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.company_name


class SignupForm_owner(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=30, widget=forms.TextInput)
    email = forms.EmailField(label='Email address', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    company_name = forms.CharField(label='company', widget=forms.TextInput, max_length=30)  
    contact = forms.CharField(label='contact', widget=forms.TextInput, max_length=15)

    class Meta:
        model = owner
        fields = ('first_name', 'email', 'password1', 'password2', 'company_name', 'contact')



class SignupForm_manager(UserCreationForm):

    first_name = forms.CharField(label='First name', max_length=30, widget=forms.TextInput)
    email = forms.EmailField(label='Email address', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    company_name = MyModelChoiceField(queryset=owner.objects.filter(is_active=True),empty_label="")
    contact = forms.CharField(label='contact', widget=forms.TextInput, max_length=15)

    class Meta:
        model = manager
        fields = ('first_name', 'email', 'password1', 'password2', 'company_name', 'contact')



class SignupForm_employee(UserCreationForm):

    first_name = forms.CharField(label='First name', max_length=30, widget=forms.TextInput)
    email = forms.EmailField(label='Email address', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    company_name = MyModelChoiceField(queryset=owner.objects.filter(is_active=True),empty_label="")
    contact = forms.CharField(label='contact', widget=forms.TextInput, max_length=15)

    class Meta:
        model = employee
        fields = ('first_name', 'email', 'password1', 'password2', 'company_name', 'contact')





class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New password",widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-3'}),strip=False)

    new_password2 = forms.CharField(label="Confirm New password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = '__all__'
