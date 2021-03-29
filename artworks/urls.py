from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artworks, name='artworks'),
    path('<int:artwork_id>/', views.artwork_detail, name='artwork_detail'),
    path('add/', views.add_artwork, name='add_artwork'),
    path('edit/<int:artwork_id>/', views.edit_artwork, name='edit_artwork'),
    path('delete/<int:artwork_id>/', views.delete_artwork,
         name='delete_artwork'),
    path('sold/', views.sold_artwork, name='sold_artwork'),
    path('my_sales/', views.my_sales, name='my_sales'),
]
