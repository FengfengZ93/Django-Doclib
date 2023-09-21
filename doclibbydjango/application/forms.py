from django import forms
from .models import UserHealthData

class FUserHealthDatareationForm(forms.ModelForm):
    class Meta:
        model = UserHealthData
        fields = 'all'