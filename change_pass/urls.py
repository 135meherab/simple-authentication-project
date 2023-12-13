from django.urls import path
from . import views
urlpatterns = [
    path('change_with_old/', views.change_with_old, name='change_with_old'),
    path('change_without_old/', views.change_without_old, name='change_without_old')
]
