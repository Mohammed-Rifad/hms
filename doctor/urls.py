from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('home', views.doctor_home, name='dr_home'), 
    path('profile', views.profile, name='dr_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('appointment/', views.appointment, name='appointment'),
    path('patients/',views.patient_search,name='search-pt'),
    path('change_password',views.change_password,name='change_pswd'),
    path('consulting',views.consulting,name='consulting')
]