# Employee Data Management System

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![DRF](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)

A comprehensive Django REST Framework application for generating, managing, and analyzing employee data with PostgreSQL backend and API documentation.

---

## 🚀 Features

- **Data Generation**: Synthetic employee data using Faker library
- **Database Models**:
  - Employees with personal/professional details
  - Departments with budgeting
  - Positions with salary ranges
  - Performance reviews
  - Attendance tracking
- **REST API**: Full CRUD operations with filtering
- **Analytics Endpoints**: Department statistics and employee performance metrics
- **Swagger UI**: Interactive API documentation
- **Admin Interface**: Built-in Django admin for data management
- **Authentication**: Basic and Session authentication
- **Rate Limiting**: 100 requests/hour per user

---

## 🏗️ System Architecture

```
employee_data_project/
├── employee_data/             # Main app
│   ├── models.py              # Database models
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views
│   ├── urls.py                # App URLs
│   └── utils.py               # Data generation logic
├── employee_data_project/     # Project config
│   ├── settings.py            # Django settings
│   └── urls.py                # Root URLs
└── manage.py                  # Django CLI
```

---

## ⚙️ Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip 20+

---

## 🧪 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/employee-data-project.git
cd employee-data-project
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

Create a PostgreSQL database:
```sql
CREATE DATABASE employee_data;
```

Update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employee_data',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

---

## 🏃 Running the Application

```bash
python manage.py runserver
```

- Admin Interface: http://localhost:8000/admin  
- API Documentation (Swagger): http://localhost:8000/swagger  
- API Root: http://localhost:8000/

---

## 📊 Generating Sample Data

### Option 1: API Call

Make an authenticated `POST` request to:

```
POST /generate-sample-data/
```

### Option 2: Django Shell

```bash
python manage.py shell
```

```python
from employee_data.utils import generate_sample_data
generate_sample_data()
```

---

## 📡 API Endpoints

| Endpoint                     | Method(s)         | Description                     |
|-----------------------------|-------------------|---------------------------------|
| `/employees/`               | GET, POST         | List/Create employees           |
| `/employees/{id}/`          | GET, PUT, DELETE  | Employee details                |
| `/department-stats/`        | GET               | Department analytics            |
| `/employee-performance/`    | GET               | Performance metrics             |

---

## 🔐 Environment Variables

Create a `.env` file:

```ini
DB_NAME=employee_data
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-django-secret-key
```

---

## ✅ Testing

Run the following command:

```bash
python manage.py test
```

---

## 🚀 Deployment Notes

- Set `DEBUG = False` in `settings.py`
- Use environment variables for sensitive data
- Set up Gunicorn/Nginx for production server
- Secure the authentication mechanism
- Configure PostgreSQL credentials properly

---

## 🤝 Contributing

1. Fork the repository  
2. Create your branch:  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:  
   ```bash
   git commit -am 'Add feature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request

---


