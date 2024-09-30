from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalRecord
from .forms import MedicalRecordForm, MedicalRecordEditForm
from reception.models import Patient


def patient_records(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id) 
    records = MedicalRecord.objects.filter(patient=patient) 
    return render(request, 'doctor/patient_records.html', {'patient': patient, 'records': records})

def add_record(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient  
            record.save()
            return redirect('patient_records', patient_id=patient.id)
    else:
        form = MedicalRecordForm()
    return render(request, 'doctor/add_record.html', {'form': form, 'patient': patient})


def edit_record(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('patient_records', patient_id=record.patient.id)
    else:
        form = MedicalRecordForm(instance=record)
    
    return render(request, 'doctor/edit_record.html', {
        'form': form,
        'record': record,
        'patient': record.patient 
    })

def delete_record(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('patient_records', patient_id=record.patient.id)
    return render(request, 'doctor/delete_record.html', {'record': record})

def patient_list(request):
    patients = Patient.objects.all() 
    return render(request, 'doctor/patient_records.html', {'patients': patients})

def doctor_landing_page(request):
    patients = Patient.objects.all()  
    return render(request, 'doctor/patient_list.html', {'patients': patients})

