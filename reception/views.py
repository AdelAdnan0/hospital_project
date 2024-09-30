from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientRegistrationForm, PatientEditForm


def patient_list(request):
    gender_filter = request.GET.get('gender')

    if gender_filter:
        patients = Patient.objects.filter(gender__iexact=gender_filter)
    else:
        patients = Patient.objects.all()

    return render(request, 'reception/patient_list.html', {'patients': patients})

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientRegistrationForm()
    return render(request, 'reception/register_patient.html', {'form': form})

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientEditForm(instance=patient)
    return render(request, 'reception/edit_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'reception/delete_patient.html', {'patient': patient})
