from django.contrib import admin
from .models import User,Course,Subject

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Subject)