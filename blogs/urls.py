from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='blogs-frontship'),
    path('Home/', views.home, name='blogs-home'),
   # path('frontship/', views.front, name='blogs-frontship'),
    path('register/', views.add, name='blogs-register'),
    path('register-2/', views.registers, name='blogs-register-2'),
    path('dashboard-2/', views.dash_two, name='blogs-dashboard-2'),
    path('dashboard/', views.dashboard, name='blogs-dashboard'),
    path('free-ship/', views.free_ship, name='blogs-free'),
    path('Predictions/', views.prediction, name='blogs-prediction'),
]


'''
[{% for dess in des %} '{{ dess.orgin }}', {% endfor %}]
'''