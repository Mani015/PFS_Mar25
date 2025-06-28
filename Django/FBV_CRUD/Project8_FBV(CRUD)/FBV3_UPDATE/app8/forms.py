from django import forms
from app8.models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"

