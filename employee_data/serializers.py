from rest_framework import serializers
from .models import Department, Position, Employee, PerformanceReview, Attendance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    
    class Meta:
        model = Employee
        fields = '__all__'

class PerformanceReviewSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = PerformanceReview
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = Attendance
        fields = '__all__'

class DepartmentStatsSerializer(serializers.Serializer):
    department = DepartmentSerializer()
    employee_count = serializers.IntegerField()
    avg_salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    avg_performance = serializers.DecimalField(max_digits=3, decimal_places=1)

class EmployeePerformanceSerializer(serializers.Serializer):
    employee = EmployeeSerializer()
    avg_rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    attendance_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)