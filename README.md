# Employee Data Management System

A Django REST Framework application for managing employee data.

## Features
- Employee data generation
- PostgreSQL database
- REST API endpoints
- Swagger documentation
- Admin interface

## Setup
1. Clone repo:
   ```bash
   git clone https://github.com/yourusername/employee-data-project.git
   ```
2. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Running
```bash
python manage.py runserver
```
- Admin: http://localhost:8000/admin
- API Docs: http://localhost:8000/swagger
