from django.urls import path 

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("collections/", views.collection_list, name="collection_list"),
    path('add_to_collection/', views.add_to_collection, name='add_to_collection'),
    path('delete_image_from_collection/', views.delete_image_from_collection, name='delete_image_from_collection'),
    path("collection_detail/", views.collection_detail, name="collection_detail"),
]