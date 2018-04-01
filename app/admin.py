from django.contrib import admin

# Register your models here.
from app.models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'rank', 'photo')
    fields = ('name', 'position', 'rank', 'photo')


admin.site.register(Person, PersonAdmin)
