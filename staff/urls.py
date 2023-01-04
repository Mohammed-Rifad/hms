from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('home', views.staff_home, name='staff_home'),
     
    path('appointments/', views.appointments, name='app-list'),
    path('patient_search/', views.pt_search, name='pt-search'), 
    path('staff/', views.staff_list, name = 'staff-list'),
    path('profile/', views.profile, name="staff-prof")
]
