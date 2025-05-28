from faker import Faker
import random
from datetime import datetime, timedelta
from .models import Department, Position, Employee, PerformanceReview, Attendance

fake = Faker()

def generate_departments(count=3):
    departments = []
    for _ in range(count):
        dept = Department.objects.create(
            name=fake.company_suffix() + " Department",
            location=fake.city(),
            budget=random.randint(100000, 1000000),
            established_date=fake.date_between(start_date='-10y', end_date='-1y'),
            manager_position=fake.job(),
            description=fake.paragraph()
        )
        departments.append(dept)
    return departments

def generate_positions(departments, count_per_dept=2):
    positions = []
    for dept in departments:
        for _ in range(count_per_dept):
            min_salary = random.randint(30000, 80000)
            max_salary = min_salary + random.randint(10000, 30000)
            pos = Position.objects.create(
                title=fake.job(),
                department=dept,
                salary_range_min=min_salary,
                salary_range_max=max_salary,
                is_managerial=random.choice([True, False]),
                requirements=fake.paragraph(),
                benefits=fake.paragraph(),
                remote_available=random.choice([True, False])
            )
            positions.append(pos)
    return positions

def generate_employees(positions, count=5):
    employees = []
    for _ in range(count):
        position = random.choice(positions)
        salary = random.randint(position.salary_range_min, position.salary_range_max)
        emp = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            hire_date=fake.date_between(start_date='-5y', end_date='today'),
            position=position,
            salary=salary,
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.postcode()
        )
        employees.append(emp)
    return employees

def generate_performance_reviews(employees, count_per_employee=2):
    reviews = []
    for emp in employees:
        for _ in range(count_per_employee):
            review_date = fake.date_between(
                start_date=emp.hire_date,
                end_date='today'
            )
            review = PerformanceReview.objects.create(
                employee=emp,
                review_date=review_date,
                reviewer=fake.name(),
                rating=random.randint(1, 5),
                comments=fake.paragraph(),
                goals_achieved=fake.paragraph(),
                areas_for_improvement=fake.paragraph(),
                next_review_date=review_date + timedelta(days=365)
            )
            reviews.append(review)
    return reviews

def generate_attendance_records(employees, days=30):
    attendance = []
    for emp in employees:
        for day in range(days):
            date = datetime.now() - timedelta(days=day)
            if random.random() > 0.1:  # 90% chance of being present
                check_in = fake.time_object()
                status = random.choice(['present', 'late', 'half_day'])
                if status == 'half_day':
                    check_out = (datetime.combine(date, check_in) + timedelta(hours=4)).time()
                else:
                    check_out = (datetime.combine(date, check_in) + timedelta(hours=8)).time()
            else:
                check_in = None
                check_out = None
                status = random.choice(['absent', 'on_leave'])
            
            att = Attendance.objects.create(
                employee=emp,
                date=date,
                check_in=check_in,
                check_out=check_out,
                status=status,
                notes=fake.sentence() if status != 'present' else ''
            )
            attendance.append(att)
    return attendance

def generate_sample_data():
    departments = generate_departments()
    positions = generate_positions(departments)
    employees = generate_employees(positions)
    reviews = generate_performance_reviews(employees)
    attendance = generate_attendance_records(employees)
    return {
        'departments': departments,
        'positions': positions,
        'employees': employees,
        'reviews': reviews,
        'attendance': attendance
    }