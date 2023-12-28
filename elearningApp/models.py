from django.db import models

 


# Create your models here.


# Courses Categories:
class CoursesCategories(models.Model):
    image = models.ImageField(upload_to="CoursesCat")
    categories = models.CharField(max_length=20)
    no_of_courses = models.IntegerField(default=0)
    
    def __str__(self):
        return self.categories
    
# Popular Courses Model here:
class PopularCourse(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="UploadedIages", default="./course-1.jpg")
    number_of_students = models.IntegerField()
    course_duration = models.DurationField()
    instructor = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    