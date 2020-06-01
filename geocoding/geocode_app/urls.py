from django.urls import path
from geocode_app import views

urlpatterns = [
    path('home/', views.home, name='data'),
]
