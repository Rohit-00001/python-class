from django.contrib import admin
from travel.models import UserData

class TravelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

admin.site.register(UserData , TravelAdmin)
