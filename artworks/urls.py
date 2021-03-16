from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artworks, name='artworks'),
    path('<int:artwork_id>', views.artwork_detail, name='artwork_detail'),
]
