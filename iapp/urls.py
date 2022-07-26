from  .import views
from django.urls import path

urlpatterns =[
    path('',views.first,name='first'),
    path('table',views.addleads,name='addleads')
]