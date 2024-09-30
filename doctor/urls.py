from django.urls import path
from . import views
from .views import add_record, doctor_landing_page, patient_list, patient_records  

urlpatterns = [
    path('', doctor_landing_page, name='doctor_landing'), 
    path('records/<int:patient_id>/', patient_records, name='patient_records'),
    path('records/<int:patient_id>/add/', add_record, name='add_record'),
    path('records/<int:patient_id>/', patient_records, name='patient_records'),  
    path('records/<int:patient_id>/add/', add_record, name='add_record'), 
    path('records/<int:patient_id>/', patient_records, name='patient_records'),  
    path('records/<int:patient_id>/add/', add_record, name='add_record'), 
    path('', patient_list, name='doctor_patient_list'),
    path('records/<int:patient_id>/', views.patient_records, name='patient_records'),  
    path('records/<int:patient_id>/add/', views.add_record, name='add_record'),
    path('records/edit/<int:record_id>/', views.edit_record, name='edit_record'),  
    path('records/delete/<int:record_id>/', views.delete_record, name='delete_record'), 
]
