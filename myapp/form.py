from django.forms import ModelForm
from myapp.models import Fleet

class FleetForm(ModelForm):
    class Meta:
        model = Fleet
        fields = ('name', 'text', )
