Hospital Management System
==========================

This project is a Hospital Management System built using Django. It contains two main apps:

1.  **Reception**: Responsible for patient management (adding, updating, and deleting patient information).
2.  **Doctor**: Manages patient diagnoses and medical records (adding, viewing, editing, and deleting medical records).

English Version
---------------

### Features

-   **Reception App**:\
    Allows the receptionists to add, edit, and delete patient information.

-   **Doctor App**:\
    Enables doctors to manage patient diagnoses and medical records, including adding new records, updating existing ones, and deleting them.

### Prerequisites

-   Python 3.x
-   Django 4.x or later

### Installation Steps

#### Step 1: Install Python

If you don't have Python installed, download and install Python 3.x from the official Python website:\
<https://www.python.org/downloads/>

Ensure Python is added to your system's PATH.

#### Step 2: Install Django and Other Required Libraries

1.  Open the terminal (command prompt) and navigate to the project directory:

    bash

    Copy code

    `cd path_to_your_project`

2.  Set up a virtual environment (optional but recommended):

    bash

    Copy code

    `python -m venv venv`

3.  Activate the virtual environment:

    -   **Windows**:

        bash

        Copy code

        `venv\Scripts\activate`

    -   **Mac/Linux**:

        bash

        Copy code

        `source venv/bin/activate`

4.  Install Django and other required packages using `pip`:

    bash

    Copy code

    `pip install -r requirements.txt`

    If there's no `requirements.txt` file, install Django manually:

    bash

    Copy code

    `pip install django`

#### Step 3: Database Migration

Run the following commands to set up the database:

bash

Copy code

`python manage.py migrate`

#### Step 4: Run the Development Server

To start the project, run:

bash

Copy code

`python manage.py runserver`

This will start the Django development server. Open your browser and go to:

bash

Copy code

`http://127.0.0.1:8000/`

#### Step 5: Access the Applications

-   **Reception App**:\
    Manage patients:\
    Access it via the following URL:\
    `http://127.0.0.1:8000/reception/`

-   **Doctor App**:\
    Manage medical records and diagnoses:\
    Access it via the following URL:\
    `http://127.0.0.1:8000/doctor/`

### Project Structure

-   **hospital_project/**: The main Django project directory.
    -   `settings.py`: Project settings.
    -   `urls.py`: Global URL configurations.
-   **reception/**: The reception app for managing patients.
    -   `models.py`: Defines the patient model.
    -   `views.py`: Handles the logic for managing patients.
-   **doctor/**: The doctor app for managing medical records.
    -   `models.py`: Defines the medical records model.
    -   `views.py`: Handles the logic for managing diagnoses.

* * * * *

النسخة العربية
--------------

### الميزات

-   **تطبيق الاستقبال**:\
    يسمح لموظفي الاستقبال بإضافة وتعديل وحذف بيانات المرضى.

-   **تطبيق الطبيب**:\
    يُمكّن الأطباء من إدارة تشخيصات المرضى وسجلاتهم الطبية، بما في ذلك إضافة سجلات جديدة، وتحديثها، وحذفها.

### المتطلبات الأساسية

-   بايثون 3.x
-   جانغو 4.x أو أحدث

### خطوات التثبيت

#### الخطوة 1: تثبيت بايثون

إذا لم يكن لديك بايثون مثبتًا، قم بتحميل وتثبيت الإصدار 3.x من الموقع الرسمي:\
<https://www.python.org/downloads/>

تأكد من إضافة Python إلى مسار النظام (PATH).

#### الخطوة 2: تثبيت Django والمكتبات الأخرى المطلوبة

1.  افتح نافذة الأوامر وانتقل إلى مجلد المشروع:

    bash

    Copy code

    `cd path_to_your_project`

2.  إعداد بيئة افتراضية (اختياري لكنه موصى به):

    bash

    Copy code

    `python -m venv venv`

3.  تفعيل البيئة الافتراضية:

    -   **Windows**:

        bash

        Copy code

        `venv\Scripts\activate`

    -   **Mac/Linux**:

        bash

        Copy code

        `source venv/bin/activate`

4.  تثبيت Django وبقية الحزم المطلوبة باستخدام `pip`:

    bash

    Copy code

    `pip install -r requirements.txt`

    إذا لم يكن هناك ملف `requirements.txt`، قم بتثبيت Django يدويًا:

    bash

    Copy code

    `pip install django`

#### الخطوة 3: إجراء ترحيل قاعدة البيانات

لتكوين قاعدة البيانات، قم بتنفيذ الأوامر التالية:

bash

Copy code

`python manage.py migrate`

#### الخطوة 4: تشغيل خادم التطوير

لتشغيل المشروع، نفّذ الأمر التالي:

bash

Copy code

`python manage.py runserver`

سيتم تشغيل خادم تطوير Django. افتح المتصفح وانتقل إلى:

bash

Copy code

`http://127.0.0.1:8000/`

#### الخطوة 5: الوصول إلى التطبيقات

-   **تطبيق الاستقبال**:\
    لإدارة المرضى:\
    ادخل على الرابط التالي:\
    `http://127.0.0.1:8000/reception/`

-   **تطبيق الطبيب**:\
    لإدارة السجلات الطبية والتشخيصات:\
    ادخل على الرابط التالي:\
    `http://127.0.0.1:8000/doctor/`

### هيكل المشروع

-   **hospital_project/**: مجلد المشروع الرئيسي.
    -   `settings.py`: إعدادات المشروع.
    -   `urls.py`: تكوينات عناوين URL.
-   **reception/**: تطبيق الاستقبال لإدارة المرضى.
    -   `models.py`: يحتوي على نموذج بيانات المرضى.
    -   `views.py`: يحتوي على المنطق لإدارة المرضى.
-   **doctor/**: تطبيق الطبيب لإدارة السجلات الطبية.
    -   `models.py`: يحتوي على نموذج بيانات السجلات الطبية.
    -   `views.py`: يحتوي على المنطق لإدارة التشخيصات.
