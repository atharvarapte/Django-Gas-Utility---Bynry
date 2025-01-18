from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.http import HttpResponse


def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/create_request.html', {'form': form})

def track_request(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'customer_service/track_request.html', {'requests': requests})

def request_details(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'customer_service/request_details.html', {'service_request': service_request})


def home(request):
    return HttpResponse("<h1>Welcome to the Gas Utility Service Application</h1><p><a href='/service/create/'>Create Service Request</a></p><p><a href='/service/track/'>Track Service Requests</a></p>")
