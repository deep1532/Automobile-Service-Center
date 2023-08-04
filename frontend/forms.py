from django import forms
from frontend.models import EmpModel

class Customerforms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields="__all__"