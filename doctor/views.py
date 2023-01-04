from django.shortcuts import render,redirect
from hms_admin.models import Doctor
# Create your views here.
def doctor_home(request):
    doctor = Doctor.objects.filter(id = request.session['doctor']).values('doctor_name')
    doc_name = doctor[0]['doctor_name']
    return render(request,'doctor/doctor_home.html', {'doc_name' : doc_name})

def profile(request):
    doctor = Doctor.objects.get(id = request.session['doctor'])
    return render(request,'doctor/profile.html', {'doctor': doctor})

def edit_profile(request):
    doctor = Doctor.objects.get(id = request.session['doctor'])
    
    if request.method == 'POST':
        name = request.POST['dr_name']
        email = request.POST['dr_email']
        contact = request.POST['dr_contact']
        qualification = request.POST['dr_qual']
        experience = request.POST['dr_exp']
        fee = request.POST['dr_fee']

        doctor = Doctor.objects.get(id = request.session['doctor'])
        doctor.doctor_name = name
        doctor.doctor_email = email
        doctor.doctor_contact = contact
        doctor.qualification = qualification
        doctor.experience = experience
        doctor.fee = fee
        doctor.save()
        return redirect('doctor:dr_profile')

    return render(request,'doctor/edit_profile.html', {'doctor': doctor})

def appointment(request):
    return render(request,'doctor/appointment.html')

def patient_search(request):
    return render(request,'doctor/pt_search.html')

def change_password(request):

    error_msg = ''
    success_msg =''
    
    if request.method == 'POST':

        old_password = request.POST['old_passwd']
        new_password = request.POST['new_passwd']
        confirm_password = request.POST['confirm_passwd']
        doctor = Doctor.objects.get(id = request.session['doctor']) # getting doctor details 
        print(old_password)
        if doctor.password == old_password :

            if new_password == confirm_password :

                if len(new_password) > 8 :
                    doctor.password = new_password
                    doctor.save()
                    success_msg = 'Password Changed'
                else :
                    error_msg = 'Password Should Be Min 8 Characters'

            else:
                error_msg = 'Password Doesnt Match'
            
        else :
            error_msg = 'Invalid Password'

    return render(request,'doctor/change_paswd.html', {'error_msg' : error_msg, 'success_msg' : success_msg})

def consulting(request):
    return render(request,'doctor/consulting.html')
