from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Rental,Area,Poi,Post,Like,Leaf


class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField:{
            'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})
        }
    }


admin.site.register(Rental, RentalAdmin)
admin.site.register(Area)
admin.site.register(Poi)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Leaf)