from django.contrib import admin

# Register your models here.

from .models import (
    Inmate,
    Gang,
    PrisonFacility,
    CellBlock,
    PrisonCell,
    Officer,
    MedicalRecord,
    FinancialRecord
)

class InmateAdmin(admin.ModelAdmin):

    list_display = ('last_name', 'first_name',
                    'days_til_release', 'release_date')

    def days_til_release(self, obj):
        return str(obj.time_to_release())

    days_til_release.short_description = 'Days Until Release'
    list_filter = ('first_name', 'last_name', 'release_date')

    ordering = ("release_date",)


class PrisonFacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')

class PrisonCellAdmin(admin.ModelAdmin):
    def block_number(self, obj):
        return obj.cell_block.block_number
    block_number.short_description = 'cell block'

    def facility(self, obj):
        return obj.cell_block.facility.name
    facility.short_description = 'facility'

    list_display = ('cell_number', 'block_number', 'facility')
    list_filter = ('cell_number',)

admin.site.register(Inmate, InmateAdmin)
admin.site.register(Gang)
admin.site.register(PrisonFacility, PrisonFacilityAdmin)
# admin.site.register(CellBlock)
admin.site.register(PrisonCell, PrisonCellAdmin)
admin.site.register(Officer)
# admin.site.register(MedicalRecord)
# admin.site.register(FinancialRecord)
