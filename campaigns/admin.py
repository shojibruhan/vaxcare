from django.contrib import admin
from .models import Vaccine, Booking

# Register your models here.
@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display= ['id', 'vaccine_name']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display= ['id', 'vaccine']


# admin.site.register(Vaccine)
# admin.site.register(Booking)