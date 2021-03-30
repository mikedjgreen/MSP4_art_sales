from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_members, name='view_members'),
    path('<int:member_id>/', views.member_details, name='member_details'),
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    path('paysub/', views.pay_subs, name='pay_subs'),
    path('delete/<int:member_id>/', views.delete_member,
         name='delete_member'),
]
