from django.shortcuts import render
from .models import CoursesCategories, PopularCourse

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def team(request):
    return render(request, "team.html", {})

def contact(request):
    return render(request, "contact.html", {})

def courses(request):
    coursescategory = CoursesCategories.objects.all()
    popcourse = PopularCourse.objects.all()
    return render(request, "courses.html", {'popcourse':popcourse, 'coursescategory':coursescategory})

def testimonial(request):
    return render(request, "testimonial.html", {})