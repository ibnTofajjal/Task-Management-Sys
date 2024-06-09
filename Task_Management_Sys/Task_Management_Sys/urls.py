
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('task/', include("Task.urls")),
    path('category/', include("Category.urls")),
]
