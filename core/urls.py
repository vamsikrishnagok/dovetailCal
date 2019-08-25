from django.urls import path
from .views import *

app_name = "core"
urlpatterns = [
    path('test/', test, name="test"),
    path('dovetail/', dovetail, name="dovetail")

]
