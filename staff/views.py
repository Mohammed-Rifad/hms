from django.shortcuts import render

# Create your views here.
def staff_home(request):
    return render(request,'staff/staff_home.html')



def appointments(request):
    return render(request,'staff/appointments.html')

def pt_search(request):
    return render(request,'staff/patient_search.html')
   
def staff_list(request):
    return render(request,'staff/staff.html')

def profile(request):
    return render(request,'staff/staff_profile.html')
