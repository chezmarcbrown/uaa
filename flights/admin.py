from django.contrib import admin

from .models import Airport, Flight

admin.site.register(Airport)
#admin.site.register(Flight)

class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "duration")

admin.site.register(Flight, FlightAdmin)