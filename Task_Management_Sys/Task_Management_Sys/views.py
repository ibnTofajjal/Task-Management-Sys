from django.http import HttpResponse
from django.shortcuts import render
from Task import models

def home(request):
    task = models.TaskModel.objects.all()
    return render(request, "home.html", {"tasks": task})