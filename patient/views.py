from django.shortcuts import render,redirect
from common.models import Patient
from . models import Booking
from hms_admin.models import Department,Doctor,Consultation
from datetime import datetime
from random import randint
from .services import get_slots,create_slots
from django.http import JsonResponse,HttpResponse
# Create your views here.
def home(request):
    patient = Patient.objects.filter(id = request.session['patient']).values('patient_name')
    pat_name = patient[0]['patient_name']
    return render(request,'patient/patient_home.html', {'pat_name' : pat_name})

def appointment(request): # old appointment
    return render(request,'patient/appointment.html')

def confirmation(request): # old confirmation
    return render(request,'patient/confirmation.html')

def my_bookings(request):
    return render(request,'patient/my_bookings.html')

def prescriptions(request):
    return render(request,'patient/prescriptions.html')

def change_password(request):

    error_msg = ''
    success_msg = ''

    if request.method == 'POST':

        old_password = request.POST['old_pswd']
        new_password = request.POST['new_pswd']
        confirm_password = request.POST['confirm_pswd']
        patient = Patient.objects.get(id = request.session['patient']) # getting patient details
        print(old_password)
        if patient.password == old_password :

            if new_password == confirm_password :

                if len(new_password) > 8 :
                    patient.password = new_password
                    patient.save()
                    success_msg = 'your password has changed'
                else :
                    error_msg = 'your password shold be minimum 8 characters'
            else :
                error_msg = 'password doesnt match'           
        else :
            error_msg = 'Invalid password'  

    return render(request,'patient/pt_change-password.html',{'error_msg' : error_msg, 'success_msg' : success_msg})

def patient_profile(request):
    patient_profile = Patient.objects.get(id = request.session['patient'])
    return render(request,'patient/patient_profile.html', {'patient': patient_profile})

def register(request):
    return render(request,'patient/register.html')

def patient_edit(request):

    if request.method == 'POST':
        patient_edit = Patient.objects.get(id = request.session['patient'])
        patient_edit.patient_name = request.POST['p_name']
        patient_edit.address = request.POST['p_address']
        patient_edit.age = request.POST['p_age']
        patient_edit.gender = request.POST['p_gender']
        patient_edit.blood_grp = request.POST['blood_grp']
        patient_edit.phone = request.POST['phone']
        patient_edit.save()
        return redirect('patient:my-pro')
        
    patient_edit = Patient.objects.get(id = request.session['patient'])
    
    return render(request,'patient/pt_edit_profile.html', {'patient': patient_edit})

def appt_1(request):
    departments = Department.objects.all()
    availability = Consultation.objects.all()
    
    return render(request,'patient/appt_1.html', {'departments' : departments, })

def appt_2(request):

    doctor_id = request.GET['dr']
    doctor_record = Doctor.objects.get(id = doctor_id)

    consultation_record = Consultation.objects.filter(doctor = doctor_id).order_by('day').values()
    
    if request.method == 'POST' :
        pass
    
    return render(request,'patient/appt_2.html', {'doctor' :doctor_record,'consultation' : consultation_record })

def appt_3(request):

   

     
    



    if request.method == 'POST' :
        
        patient_name = request.POST['p_name']
        gender  = request.POST['gender']
        mobile = request.POST['mobile']
        age = request.POST['age']
        selected_date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d').date().strftime('%d-%m-%Y')
        dr = request.GET.get('dr')
        selected_time = request.GET.get('time')
        reference_no = 'Ref' + str(randint(1111,9999)) +'Hms' + mobile[6:10]

        new_booking  = Booking(
                        patient_id = request.session['patient'],
                        patient_name = patient_name,gender = gender,
                        mobile = mobile, age = age,
                        doctor_id = dr,booking_date = selected_date,
                        time = selected_time, reference_no = reference_no
                        )
    
        new_booking.save()
        return redirect('patient:appointment_4')
        

        


    dr_id = request.GET['dr']
    selected_time = request.GET['time']
    selected_date = datetime.strptime(request.GET['date'], '%Y-%m-%d').date().strftime('%d-%m-%Y')
    doctor = Doctor.objects.get(id = dr_id)
    doctor_name = doctor.doctor_name
    fee = doctor.fee
    department = doctor.department.department


    
    context = {
        'dr_name' : doctor_name,
        'dep' : department,  
        'selected_date' : selected_date,
        'selected_time' :selected_time,
        'fee': fee
    }

    return render(request,'patient/appt_3.html',context)

def appt_4(request):
    latest_booking = Booking.objects.filter(patient = request.session['patient']).last()
    
    doctor_name = latest_booking.doctor.doctor_name
    dep = latest_booking.doctor.department.department
    reference_no = latest_booking.reference_no
    booking_date = latest_booking.booking_date
    booking_time = latest_booking.time

    context = {
        'doctor_name' : doctor_name,
        'dep' : dep,
        'reference_no' : reference_no,
        'booking_date' : booking_date,
        'booking_time' : booking_time

    }
    return render(request,'patient/appt_4.html',  context)

def booking_history(request):
    return render(request,'patient/booking_history.html')


def get_doctors(request):
    dept_id = request.POST['id']
    doctors = Doctor.objects.filter(department = dept_id)
    data = [ {'dr_id' : dr.id,'dr_name' : dr.doctor_name} for dr in doctors]
    return JsonResponse({'doctors':data,})


def check_availability(request):

    dr_id = request.POST['dr_id']
    selected_day = request.POST['selected_day']
    
    

    
    
     
    consultation_record = Consultation.objects.filter(doctor = dr_id, day = selected_day)
    
    if consultation_record :
        available = True

        data_set = create_slots(consultation_record)
         
        return JsonResponse({'availability': available,'consultation_record' : data_set})

    else:
        available = False

        
        return JsonResponse({'availability': available,})