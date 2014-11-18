from django.contrib import admin
from koie.models import Koie, Reservation, Report, Damage, Facility, Notification, Firewood


class DamagesInline(admin.TabularInline):
    model = Damage

class FirewoodInline(admin.TabularInline):
    model = Firewood

class KoieAdmin(admin.ModelAdmin):
    inlines = [
        FirewoodInline,
    ]

class ReportAdmin(admin.ModelAdmin):
    inlines = [
        DamagesInline,
    ]


admin.site.register(Koie, KoieAdmin)
admin.site.register(Reservation)
admin.site.register(Report, ReportAdmin)
admin.site.register(Damage)
admin.site.register(Facility)
admin.site.register(Notification)
