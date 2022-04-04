"""
    form.py file
"""
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import login
from django.db.models import Q

from account.models import Profile


class RegistrationForm(forms.ModelForm):
    """
        registration form
    """
    confirm_password = forms.CharField(label="Confirm Password",
        widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': 'Confirm Password'
            }
        ))
    password = forms.CharField(label="Password",
        validators=[validate_password], widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg form-control-solid',
                'placeholder': 'Password'
                }
        ))

    class Meta:
        """
            meta class
        """
        fields = ["username", "email", "first_name", "last_name", "phone", "gender", "dob"]
        model = Profile
        widgets = {
          'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    def clean(self):
        cleaned_data = super().clean()
        confirm_password = cleaned_data.get("confirm_password")
        password = cleaned_data.get("password")
        if confirm_password != password:
            raise ValidationError({'password': "Password and confirm password does not matched."})


class LoginForm(forms.Form):
    """
        login form
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            if not Profile.objects.filter(Q(email=username) | Q(username=username)).exists():
                raise ValidationError("User does not exist with this username")
            user = Profile.objects.get(Q(email=username) | Q(username=username)).user
            if not user.check_password(password):
                raise ValidationError("Invalid password for this username.")
            if not user.is_active:
                raise ValidationError("User is not active.")
            self.user = user
            login(self.request, user)
        return self.cleaned_data
