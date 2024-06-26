from django.contrib import admin
from .models import Course,CourseVideo, CourseMaterial,Skills
# Register your models here.


admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(CourseMaterial)
admin.site.register(Skills)

