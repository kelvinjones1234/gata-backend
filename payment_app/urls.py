from django.urls import path
from .import views
from .views import LevyByDepartment, OtherDataListView

urlpatterns = [
  path('departments/', views.DepartmentListView, name='department-list'),
  path('other-data/', views.OtherDataListView, name='other-data'),
  path('fees/<int:department_id>/', LevyByDepartment.as_view(), name='levies-list'),
]