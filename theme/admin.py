from django.contrib import admin
from mezzanine_agenda.models import Event
from mezzanine_agenda.admin import EventAdmin
# Register your models here.

class MyEventAdmin(EventAdmin):
    try:
        EventAdmin.list_display.remove('admin_thumb')
    except:
        pass



admin.site.unregister(Event)
admin.site.register(Event, MyEventAdmin)