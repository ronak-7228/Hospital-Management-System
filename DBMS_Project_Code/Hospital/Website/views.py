from django.shortcuts import render

from Website.models import Doctor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctors(request):
    doctors= Doctor.objects.all()
    context={
        'doctors': doctors
    }
    return render(request, 'doctors.html', context)