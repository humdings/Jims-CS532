from django.contrib import admin

# Register your models here.

from .models import (
    Inmate,
    Gang,
    PrisonFacility,
    CellBlock,
    PrisonCell,
    Officer
)

# class InmateAdmin(admin.ModelAdmin):
#     fields = ['first name', 'last name', 'middle name']
admin.site.register(Inmate)
admin.site.register(Gang)
admin.site.register(PrisonFacility)
admin.site.register(CellBlock)
admin.site.register(PrisonCell)
admin.site.register(Officer)
