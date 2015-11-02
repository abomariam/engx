from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin
from mezzanine_agenda.models import Event
from mezzanine_agenda.admin import EventAdmin
from models import Slider

# Register your models here.

class MyEventAdmin(EventAdmin):
    try:
        EventAdmin.list_display.remove('admin_thumb')
    except:
        pass



admin.site.unregister(Event)
admin.site.register(Event, MyEventAdmin)



class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','description','created_at']

admin.site.register(Slider,SliderAdmin)