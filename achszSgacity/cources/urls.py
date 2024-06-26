from django.urls import path
from . import views

urlpatterns = [
    path('cources/', views.Cources, name='courses'),
    path('course-details/<str:name>/', views.CourseDetails, name='course_details'),
    # path('courses-list/', views.CourseList, name='course_list'),
    path('materials/', views.Materials, name='materials'),
    path('course-materials/<int:id>/<str:name>',views.CourseMaterials,name='materials'),
]
