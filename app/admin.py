from django.contrib import admin

# Register your models here.
from app.models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'rank', 'photo')
    fields = ('name', 'position', 'rank', 'photo')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('person', 'time')
    fields = ('person', 'time')


admin.site.register(Person, PersonAdmin)
admin.site.register(History,HistoryAdmin)
