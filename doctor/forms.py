from django import forms
from .models import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'diagnosis_date', 'patient']
        widgets = {
            'diagnosis': forms.Textarea(attrs={'class': 'form-control'}),
            'diagnosis_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
        }

class MedicalRecordEditForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'diagnosis_date']
        widgets = {
            'diagnosis': forms.Textarea(attrs={'class': 'form-control'}),
            'diagnosis_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
