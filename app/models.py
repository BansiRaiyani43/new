from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=USER_ROLES, default='student')
    phone_no = models.BigIntegerField(null=True, blank=True)   # optional phone number

    def __str__(self):
        return f"{self.username} ({self.role})"

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_courses')
    students = models.ManyToManyField(User, related_name='student_courses', blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"