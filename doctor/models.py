from django.db import models
from reception.models import Patient

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    diagnosis = models.TextField()
    diagnosis_date = models.DateField()

    def __str__(self):
        return f"{self.patient.name} - {self.diagnosis}"
