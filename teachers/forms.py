from django import forms
from django.contrib.auth import get_user_model

Teacher = get_user_model()

class SignUpForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0555055555',
    }))
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Niazalieva Zarema Abdurasulovna',
    }))
    subject = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mathematics',
    }))
    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat password',
    }))

    def clean(self):
        if not self.cleaned_data['password'] == self.cleaned_data['password2'] or not self.cleaned_data['password2']:
            self._errors['password2'] = self.error_class(['Password doesn\'t match'])
        if Teacher.objects.filter(phone_number=self.cleaned_data['phone_number']).exists():
            self._errors['phone_number'] = self.error_class(['Such teacher with phone number alredy exists'])
        return self.cleaned_data

    def save(self, commit=True):
        self.cleaned_data.pop('password2')
        return Teacher.objects.create_user(**self.cleaned_data)

    class Meta:
        model = Teacher
        fields = ('phone_number', 'full_name', 'subject', 'password', 'password2')


class LogInForm(forms.ModelForm):

    phone_number = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '0555055555',
    }))
    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = Teacher
        fields = ('phone_number', 'password')