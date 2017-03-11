from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Exercise
# Create your views here.
def hello_world(request):
	return render(request,'hello_world.html',{'current_time':str(datetime.now()),
})

def home(request):
	exercise_list = Exercise.objects.all()
	return render(request,'home.html',{'exercise_list':exercise_list})
