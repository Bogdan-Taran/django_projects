from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserModel

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'email', 'avatar', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            if commit:
                user.save()

            return user