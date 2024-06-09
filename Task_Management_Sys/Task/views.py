from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from Task.models import TaskModel

# Create your views here.
def add_task(request):
    if request.method == "POST":
        taks_form = forms.TaskForm(request.POST)
        if taks_form.is_valid():
            taks_form.save()
            return redirect("homepage")
        
    else:
        taks_form = forms.TaskForm()
        return render(request,"add_task.html", {"forms": taks_form})
    


def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')