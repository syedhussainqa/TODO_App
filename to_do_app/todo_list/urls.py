from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross-off/<list_id>', views.cross_off, name='cross_off'),
    path('un-cross/<list_id>', views.uncross, name='uncross'),
    path('edit/<list_id>', views.edit, name='edit'),
]
