from django.urls import path
from . import views

urlpatterns = [
    path("", views.shipment, name="main_shipment"),
    path("add/", views.add_shipment, name="add_shipment"),
    path("delete/<int:shipment_id>/", views.delete_shipment, name="delete_shipment"),
    path("edit/<int:shipment_id>/", views.edit_shipment, name="edit_shipment"),
]