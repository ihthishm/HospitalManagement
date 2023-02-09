from django.http import HttpResponse
from django.shortcuts import render
from .models import department, doctors
from .forms import BookingForm

# Create your views here.
def index(request):

    return render(request,'index.html',)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request,'booking.html',dict_form)

def Doctors(request):
    dict_docs = {
        'docs': doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request, 'contact.html')

def Departments(request):
    dict_dept = {
        'dept' : department.objects.all()
    }
    return render(request,'department.html',dict_dept)