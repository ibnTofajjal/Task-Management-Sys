from django.db import models
from Category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssigned =  models.DateField(None)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self) -> str:
        return self.taskTitle