from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import register, user_login, user_logout, student_dashboard, teacher_dashboard, admin_dashboard
from .views import course_list,add_course, edit_course,delete_course,subject_list,subject_add,subject_edit, subject_delete
urlpatterns = [ 
    path('',register,name='signup'),
    path("login/", user_login, name="login"),
    path("logout/",user_logout, name="logout"),
    path("student/dashboard/", student_dashboard, name="student_dashboard"),
    path("teacher/dashboard/", teacher_dashboard, name="teacher_dashboard"),
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path('teacher/course/',course_list, name='course_list'),
    path('teacher/create/',add_course, name='add_course'),
    path("edit_course/<int:id>/", edit_course, name='edit_course'),
    path("delete_course/<int:id>/", delete_course, name='delete_course'),
    path("subjects/<int:course_id>/", subject_list, name="subject_list"),
    path("subjects/<int:course_id>/add/", subject_add, name="add_subject"),
    path("subjects/<int:course_id>/edit/<int:id>/", subject_edit, name="subject_edit"),
    path("subjects/<int:course_id>/delete/<int:id>/", subject_delete, name="subject_delete"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
