from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='fleet_home'),
    path('fleet', views.FleetlistView.as_view(), name='fleet_list'),
    path('fleet/<int:pk>/', views.FleetView.as_view(), name='fleet_detail'),
    path('register', views.RigisterFleetView.as_view(), name='fleet_rigister'),
]