from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('team/', views.team, name = "team"),
    path('courses/', views.courses, name = "courses"),
    path('testimonial/', views.testimonial, name = "testimonial"),
]