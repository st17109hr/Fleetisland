
from myapp.form import FleetForm
from django.views import generic
from myapp.models import Fleet
from django.urls import reverse
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html', {})

class FleetlistView(generic.ListView):
    template_name = 'myapp/fleetlist.html'
    context_object_name = 'fleet_list'
    queryset = Fleet.objects.all()

class FleetView(generic.DetailView):
    model = Fleet
    template_name = 'myapp/fleet.html'

class RigisterFleetView(generic.CreateView):
    model = Fleet
    form_class = FleetForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:fleet_list')