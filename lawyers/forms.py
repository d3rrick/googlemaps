from django.contrib.gis import forms
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from .models import Rental,Leaf
from leaflet.forms.fields import PointField


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ('address', 'geolocation')
        widgets = {
            
            'geolocation': GooglePointFieldWidget,
            'address': GoogleStaticOverlayMapWidget,

        }


class LeafForm(forms.ModelForm):
    geom = PointField()
    class Meta:
        model = Leaf
        fields = ('name', 'geom')
