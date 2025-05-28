from django.contrib import admin
from .models import Department, Position, Employee, PerformanceReview, Attendance

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(PerformanceReview)
admin.site.register(Attendance)