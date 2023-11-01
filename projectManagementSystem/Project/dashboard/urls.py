from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import CreateProject

urlpatterns = [
    path('createProject/', CreateProject , name="CreateProject"),
]
