from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'performance-reviews', views.PerformanceReviewViewSet)
router.register(r'attendance', views.AttendanceViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Employee Data API",
        default_version='v1',
        description="API for employee data generation and visualization",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-sample-data/', views.GenerateSampleDataView.as_view(), name='generate-sample-data'),
    path('department-stats/', views.DepartmentStatsView.as_view(), name='department-stats'),
    path('employee-performance/', views.EmployeePerformanceView.as_view(), name='employee-performance'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]