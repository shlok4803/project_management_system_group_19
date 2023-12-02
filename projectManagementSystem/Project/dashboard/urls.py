from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('createProject/', CreateProject , name="CreateProject"),
    path('dashboard_owner/',dashboard, name='Owner_dashboard'),
]
