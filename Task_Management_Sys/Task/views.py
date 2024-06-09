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
    

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id) # Get the task object through the primary key
    task_form = forms.TaskForm(instance=task) # create a instance of the task that get through the primary key

    if request.method == "POST":
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")
        
    return render(request,"add_task.html", {"forms": task_form})
    



def delete_task(request, id):
    task = TaskModel.objects.get(pk=id) # Get the Task object through the primary key
    task.delete()
    return redirect('homepage')