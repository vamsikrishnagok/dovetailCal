from django.urls import path
from .views import *

app_name = "core"
urlpatterns = [
    path('test/', test, name="test"),
    path('', dovetail, name="dovetail"),
    path('dovetail/list', dovetailList, name="dovetailList"),
    path('dowell/', dowell, name="dowell"),
    path('dowell/list', dowellList, name="dowellList"),
    path('dovetail/<int:id>/', Dovetailview, name="Dovetailview"),
    path('cutsheet/', cutsheet, name="cutsheet"),
    path('cutsheet/list',cutsheetList,name="cutsheetList"),
    path('cutsheet/<int:id>/', cutsheetview, name="cutsheetview"),

]
