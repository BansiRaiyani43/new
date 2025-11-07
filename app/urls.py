from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import register, user_login, user_logout, student_dashboard, teacher_dashboard, admin_dashboard,course_create,course_detail
from .views import course_list
urlpatterns = [ 
    path('',register,name='signup'),
    path("login/", user_login, name="login"),
    path("logout/",user_logout, name="logout"),
    path("student/dashboard/", student_dashboard, name="student_dashboard"),
    path("teacher/dashboard/", teacher_dashboard, name="teacher_dashboard"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path('teacher/course/',course_list, name='course_list'),
    path('create/',course_create, name='course_create'),
    path('<int:course_id>/', course_detail, name='course_detail'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
