from django import forms

from school.models import Student

from bootstrap_datepicker_plus.widgets import DatePickerInput

class StudentCreateForm(forms.ModelForm):
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ivanov Ivan Ivanovich',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@example.com',
    }))
    date_of_birth = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],)
    address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '4 district, 33 town',
    }))

    def save(self, commit: bool = ...):
        return Student.objects.create(
            **self.cleaned_data
        )

    class Meta:
        model = Student
        fields = "__all__"

class StudentUpdateForm(StudentCreateForm):

    def save(self, commit: bool = ...):
        return Student.objects.update(
            **self.cleaned_data
            )