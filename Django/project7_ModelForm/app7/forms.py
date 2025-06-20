
from django import forms
from app7.models import VehicleParking
class VehicleParkingForm(forms.ModelForm):

    class Meta:

        model = VehicleParking
        fields = "__all__"

# Similar to ModelAdmin we can use the ModelForm class and make a form object linking to the fields defined under models.py


# __all__ includes all fields under the model class. You may alternatively use a tuple of field names.