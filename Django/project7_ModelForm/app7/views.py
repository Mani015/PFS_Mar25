from django.shortcuts import render
from app7.models import VehicleParking
from app7.forms import VehicleParkingForm
# Create your views here.


def vehicleParkingList(request):
    vehicle_objects = VehicleParking.objects.all()
    return render(request,'list.html',{'vehicle' : vehicle_objects})


def vehicleForm(request):
    vehicle = VehicleParkingForm()
    if request.method == "POST":
        veh =VehicleParkingForm(request.POST)
        if veh.is_valid():
            veh.save()
        return index('/')
    return render(request,'form.html',{'form' : vehicle})


def index(request):
    return render(request,'index.html')

def sucess(request):
    return render(request,'sucess.html')
