from django.shortcuts import render
from mezzanine_agenda.models import Event
from models import Slider
from mezzanine.blog.models import BlogCategory,BlogPost

# Create your views here.

def home(request):
    context = {}

    context['events'] = Event.objects.all().order_by('-start')[:3]
    context['hide_right'] = True

    context['slider'] = Slider.objects.all()[:4]

    context['articles'] = BlogCategory.objects.get(title='articles').blogposts.all().order_by('-created')[:3]

    context['news'] = BlogCategory.objects.get(title='News').blogposts.all()[:4]

    return render(request,'index.html',context)
