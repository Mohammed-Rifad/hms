from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('home', views.home, name='home'),
    path('appointment', views.appointment, name='appointment'),
    path('confirmation', views.confirmation, name='confirm'),
    path('my-bookings', views.my_bookings, name='bookings'),
    path('my-prescriptions', views.prescriptions, name='prescriptions'),
    path('change-password', views.change_password, name='chg-pwd'),
    path('my-profile', views.patient_profile, name='my-pro'),
    path('register', views.register, name='pt_reg'),
    path('edit_patient_profile', views.patient_edit, name='edit'),
    path('appointment-1', views.appt_1, name='appointment_1'),
    path('appointment-2', views.appt_2, name='appointment_2'),
    path('appointment-3', views.appt_3, name='appointment_3'),
    path('booking-confirmation', views.appt_4, name='appointment_4'),
    path('appointment-list', views.appt_list, name='appointment_list'),
    path('get-doctors', views.get_doctors, name='get_doctors'),
    path('check-availability', views.check_availability, name='check-availability')

]
