from django.contrib import admin

# Register your models here.

from .models import Inmate

# class InmateAdmin(admin.ModelAdmin):
#     fields = ['first name', 'last name', 'middle name']

admin.site.register(Inmate,
                    # InmateAdmin
                    )
# admin.site.register(Address)

