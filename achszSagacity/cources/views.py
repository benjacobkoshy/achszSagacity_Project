from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Course,CourseVideo,CourseMaterial,Skills


# Create your views here.
# def CourseList(request):
#     courses = Course.objects.all()
#     return render(request, "courses-list.html", {'courses': courses})

def Cources(request):
    courses = Course.objects.all()
    return render(request,"courses.html",{'courses': courses})



def CourseDetails(request, name):
    course = get_object_or_404(Course, name=name)
    videos_list = course.videos.all()
    paginator = Paginator(videos_list, 5)  # Show 5 videos per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'course-details.html', {'course': course, 'page_obj': page_obj})

def Materials(request):
    skills = Skills.objects.all()
    print(skills)
    return render(request, "materials.html", {'skills': skills})



def CourseMaterials(request,id,name):
    course = get_object_or_404(Course, id=id)
    materials = CourseMaterial.objects.filter(course=course)
    return render(request,'course_materials.html', {'course': course, 'materials': materials})