from django.shortcuts import redirect, render
from .models import Shipment
from .forms import ShipmentForm

# Create your views here.
def shipment(request):
    shipments = Shipment.objects.all()
    context = {'shipments':shipments}
    return render(request, 'Shipments/main_shipment.html', context)

def add_shipment(request):
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_shipment')
    else:
        form = ShipmentForm()
    
    context = {'shipmentform' : form}
    return render(request, 'Shipments/add_shipment.html', context)

def delete_shipment(request, shipment_id):
    shipment = Shipment.objects.get(id=shipment_id)
    shipment.delete()
    return redirect('main_shipment')

def edit_shipment(request, shipment_id):
    shipment = Shipment.objects.get(id=shipment_id)
    if request.method == "POST":
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('main_shipment')
    else:
        form = ShipmentForm(instance=shipment)

    context = {"shipmentform" : form}
    return render(request, "Shipments/edit_shipment.html", context)
