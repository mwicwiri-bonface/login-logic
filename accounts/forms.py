from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, AuthenticationForm
from django.forms import ModelForm, forms

from accounts.mixins import StylingFormMixin

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['country', 'last_name', 'first_name', 'email', 'username', 'password1', 'password2']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.upper()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cod = True
        if commit:
            user.save()
        return user


class UserAdminChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'country', 'password', 'is_active']

    def clean_username(self):
        data = self.cleaned_data['username']
        return data.upper()

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAuthenticationForm(StylingFormMixin):

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = username.upper()
        return username

    def clean(self):
        super().clean()
        if self.user_cache is None or self.user_cache.is_archived:
            logout(self.request)
            raise forms.ValidationError('Invalid username or password or both', code='invalid login')
