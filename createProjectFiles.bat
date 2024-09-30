@echo off

mkdir reception\templates\reception
mkdir doctor\templates\doctor
mkdir static\css
mkdir templates

rem Creating missing files
copy NUL static\css\common.css
copy NUL templates\base.html

copy NUL reception\urls.py
copy NUL reception\forms.py
copy NUL reception\templates\reception\register_patient.html
copy NUL reception\templates\reception\edit_patient.html
copy NUL reception\templates\reception\delete_patient.html
copy NUL reception\templates\reception\patient_list.html

copy NUL doctor\urls.py
copy NUL doctor\forms.py
copy NUL doctor\templates\doctor\patient_records.html
copy NUL doctor\templates\doctor\add_record.html
copy NUL doctor\templates\doctor\edit_record.html
copy NUL doctor\templates\doctor\delete_record.html
copy NUL doctor\templates\doctor\filter_patients.html

echo Missing files and folders created successfully.
pause
