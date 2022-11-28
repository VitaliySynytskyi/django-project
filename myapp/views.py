from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.db import models
from .models import *
from .forms import *
# Create your views here.

def home(request):
    form= Form1(request.POST or None)
    print(request.POST)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, "home.htm", context)


def logs(request):
    data1 = Logs1.objects.all()
    data = {
       "Logs": data1,
    }
    return render(request, "logs.htm", data)


def list(request):
    data2 = Cabinets.objects.all()
    data = {
       "Cabinets": data2,
    }
    return render(request, "list.htm", data)

