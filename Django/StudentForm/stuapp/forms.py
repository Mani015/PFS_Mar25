
from django import forms
from stuapp.models import StudentModel


class Student(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = "__all__"


