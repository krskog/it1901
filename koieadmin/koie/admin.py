from django.contrib import admin
from koie.models import Koie, Reservation, Report, Damage, Facility


class DamagesInline(admin.TabularInline):
    model = Damage

class ReportAdmin(admin.ModelAdmin):
    inlines = [
        DamagesInline,
    ]


admin.site.register(Koie)
admin.site.register(Reservation)
admin.site.register(Report, ReportAdmin)
admin.site.register(Damage)
admin.site.register(Facility)
