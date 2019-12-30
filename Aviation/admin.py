from django.contrib import admin
from Aviation.models import Airfield, Airplane, Flight, Reservation


class AirfieldAdmin(admin.ModelAdmin):
    search_fields = ('name', 'icao')
    list_display = ('name', 'icao')

admin.site.register(Airfield, AirfieldAdmin)


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('callsign', 'mf_type', 'owner')

admin.site.register(Airplane, AirplaneAdmin)


class FlightAdmin(admin.ModelAdmin):
    date_hierarchy = 'dt_takeoff'
    list_display = (
        'airplane', 'pic', 'pic_role', 'co', 'co_role', 'attendants',
        'dt_offbl', 'dt_takeoff', 'dt_landing', 'dt_onbl', 'pause',
        'from_af', 'to_af', 'landings', 'op_time', 'remark'
    )
    list_filter = ('airplane', 'pic', 'from_af', 'to_af')

admin.site.register(Flight, FlightAdmin)


class ReservationAdmin(admin.ModelAdmin):
    date_hierarchy = 'begin'
    list_display = ('airplane', 'user', 'begin', 'end', 'remark')
    list_filter = ('airplane', 'user')

admin.site.register(Reservation, ReservationAdmin)
