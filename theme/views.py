from django.shortcuts import render
from mezzanine_agenda.models import Event
# Create your views here.

def home(request):
    context = {}

    context['events'] = Event.objects.all()



    return render(request,'index.html',context)
