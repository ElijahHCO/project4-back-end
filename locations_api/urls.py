from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'), 
    path('equipment/', views.EquipmentList.as_view(), name='equipment_list'),
    path('equipment/<int:pk>', views.EquipmentDetail.as_view(), name='equipment_detail'),
]