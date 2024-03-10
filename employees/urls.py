from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'), #
    path('employee-list/', views.employee_list, name='employee_list'), #
    path('add/', views.add_employee, name='add_employee'), #
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),#
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),#
    path('all-attendance/', views.all_attendance, name='all_attendance'),
    path('today-attendance/', views.today_attendance, name='today_attendance'),
    path('update_attendance/<int:pk>/', views.update_attendance, name='update_today_attendance'),

]
