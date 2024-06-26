from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    COURSE_CHOICES = [
        ('IELTS', 'IELTS'),
        ('UKVI', 'UKVI'),
        ('FLUENCY', 'Fluency'),
    ]
    name = models.CharField(max_length=50, choices=COURSE_CHOICES, unique=True)
    detailed_name = models.CharField(max_length=100)
    description = models.TextField(default="Default description")
    price = models.CharField(max_length=10,default=0)
    trainer_name = models.CharField(max_length=100,default='Achsa Jomesh')
    # trainer_image = models.ImageField(upload_to='static/mentor/')
    course_image = models.ImageField(upload_to='images/courses/',null=True)

    def __str__(self):
        return self.name
    
class CourseVideo(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField()

    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        # Extract the video ID and create an embed URL
        if "youtu.be" in self.youtube_url:
            video_id = self.youtube_url.split('/')[-1].split('?')[0]
        elif "youtube.com" in self.youtube_url:
            video_id = self.youtube_url.split('v=')[1].split('&')[0]
        else:
            video_id = None
        
        return f"https://www.youtube.com/embed/{video_id}" if video_id else self.youtube_url
    


class Skills(models.Model):
    SKILL_CHOICES = [
        ('LISTENING', 'Listening'),
        ('SPEAKING', 'Speaking'),
        ('READING', 'Reading'),
        ('WRITING','Writing'),
    ]
    name = models.CharField(max_length=50, choices=SKILL_CHOICES, unique=True)
    description = models.TextField(default="Default description")
    price = models.CharField(max_length=10,default=499)
    author_name = models.CharField(max_length=100,default='Achsa Jomesh')
    skill_image = models.ImageField(upload_to='images/courses/',null=True)

    def __str__(self):
        return self.name



class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='course_materials/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
