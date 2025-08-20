from django.urls import path
from . import views
urlpatterns=[
    path('',views.display),
    path('gettasks/',views.gettasks),
    path('modifytask/<int:pk>/',views.modifytask)
]