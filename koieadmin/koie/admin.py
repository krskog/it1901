from django.contrib import admin
from koie.models import Koie, Reservation, Report, Damage, Facility, Notification, Firewood

# Inlines
class DamagesInline(admin.TabularInline):
    model = Damage

class FirewoodInline(admin.TabularInline):
    model = Firewood

# Admins
class KoieAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'num_beds')
    search_fields = ['name', 'location', 'num_beds']
    inlines = [
        FirewoodInline,
    ]

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('koie_ordered', 'ordered_by', 'rent_date', 'ordered_date', 'beds')
    search_fields = ['koie_ordered', 'ordered_by', 'rent_date', 'ordered_date', 'beds']

class ReportAdmin(admin.ModelAdmin):
    inlines = [
        DamagesInline,
    ]

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('koie', 'due_date', 'reservation')
    search_fields = ['koie', 'due_date', 'reservation']

admin.site.register(Koie, KoieAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Damage)
admin.site.register(Facility)
admin.site.register(Notification, NotificationAdmin)
