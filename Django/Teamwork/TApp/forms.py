from django import forms
from TApp.models import Student


class  Studentform(forms.ModelForm):
    class Meta:
        model=Student

        fields='__all__'


