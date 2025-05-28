from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
from .models import Department, Position, Employee, PerformanceReview, Attendance
from .serializers import (
    DepartmentSerializer, PositionSerializer, EmployeeSerializer,
    PerformanceReviewSerializer, AttendanceSerializer,
    DepartmentStatsSerializer, EmployeePerformanceSerializer
)
from .utils import generate_sample_data
from django.db.models import Avg, Count
from datetime import date, timedelta

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    throttle_classes = [UserRateThrottle]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    throttle_classes = [UserRateThrottle]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [UserRateThrottle]
    filterset_fields = ['position', 'is_active']

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    throttle_classes = [UserRateThrottle]
    filterset_fields = ['employee', 'rating']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    throttle_classes = [UserRateThrottle]
    filterset_fields = ['employee', 'status', 'date']

class GenerateSampleDataView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        data = generate_sample_data()
        return Response({
            'message': 'Sample data generated successfully',
            'counts': {
                'departments': len(data['departments']),
                'positions': len(data['positions']),
                'employees': len(data['employees']),
                'reviews': len(data['reviews']),
                'attendance_records': len(data['attendance'])
            }
        }, status=status.HTTP_201_CREATED)

class DepartmentStatsView(generics.ListAPIView):
    serializer_class = DepartmentStatsSerializer
    
    def get_queryset(self):
        # Calculate stats for each department
        departments = Department.objects.annotate(
            employee_count=Count('position__employee'),
            avg_salary=Avg('position__employee__salary')
        )
        
        stats = []
        for dept in departments:
            avg_performance = PerformanceReview.objects.filter(
                employee__position__department=dept
            ).aggregate(avg=Avg('rating'))['avg'] or 0
            
            stats.append({
                'department': dept,
                'employee_count': dept.employee_count,
                'avg_salary': dept.avg_salary,
                'avg_performance': avg_performance
            })
        
        return stats

class EmployeePerformanceView(generics.ListAPIView):
    serializer_class = EmployeePerformanceSerializer
    
    def get_queryset(self):
        thirty_days_ago = date.today() - timedelta(days=30)
        
        employees = Employee.objects.all()
        performance_data = []
        
        for emp in employees:
            
            avg_rating = PerformanceReview.objects.filter(
                employee=emp
            ).aggregate(avg=Avg('rating'))['avg'] or 0
            
        
            total_days = Attendance.objects.filter(
                employee=emp,
                date__gte=thirty_days_ago
            ).count()
            
            present_days = Attendance.objects.filter(
                employee=emp,
                date__gte=thirty_days_ago,
                status='present'
            ).count()
            
            attendance_percentage = (present_days / total_days * 100) if total_days > 0 else 0
            
            performance_data.append({
                'employee': emp,
                'avg_rating': avg_rating,
                'attendance_percentage': attendance_percentage
            })
        
        return performance_data