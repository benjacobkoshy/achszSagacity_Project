from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from cources.models import Course

# Create your views here.
def Home(request):
    students = User.objects.count
    course_no = Course.objects.count
    courses = Course.objects.all()
    return render(request,'home.html',{'students':students, 'course_no':course_no ,'courses': courses})


def About(request):
    count = User.objects.count
    return render(request,"about.html",{'count':count})

def GetStarted(request):
    return render(request,"starter-page.html")


def Contact(request):
    if request.method == 'POST' and 'send' in request.POST:
        name = request.POST.get('name')
        email = request.user.email if request.user.is_authenticated else request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject,
                f'From: {name} <{email}>\n\n{message}',
                email,
                ['bennjacob828@gmail.com'],  # Replace with your company email
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')  # Redirect to the contact page or any other appropriate page
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, 'There was an error sending your message. Please try again later.[Check your internt connection]')
            return redirect('contact')  # Redirect to the contact page on error

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


    






def Pricing(request):
    return render(request,"pricing.html")

def Trainers(request):
    return render(request,"trainers.html")

def Events(request):
    return render(request,"events.html")

def Counts(request):
    students = User.objects.count
    course_no = Course.objects.count
    return render(request,"counts.html",{'students':students,'couses':course_no})
