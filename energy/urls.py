from django.urls import path
from . import views

app_name = 'energy'

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('<int:cus_id>/', views.rating_details, name="rating_details"),

]
