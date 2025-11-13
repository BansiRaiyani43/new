from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User, Course

# Create your views here.
User = get_user_model()

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        role = request.POST.get("role")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # ----------------- Validation -----------------
        if not username or not email or not password1 or not password2 or not role:
            messages.error(request, "Please fill in all required fields.")
            return redirect("signup")

        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:    
            user = User.objects.create_user(
            username=username,
            email=email,
            phone_no=phone_no,  
            role=role,
            password=password1
          )
            user.save()

            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
    return render(request, 'sign_up.html')
        
# ------------------ LOGIN VIEW ------------------
def user_login(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username  # Django authenticate() needs username field internally
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(request, "Your account is inactive")
                return redirect("login")
            
            login(request, user)

            # Redirect based on role
            if user.role == "student":
                return redirect("student_dashboard")
            elif user.role == "teacher":
                return redirect("teacher_dashboard")
            elif user.role == "admin":
                return redirect("admin_dashboard")
            else:
                messages.error(request, "Invalid role assigned.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

# ------------------ LOGOUT VIEW ------------------
def user_logout(request):
    logout(request)
    return redirect("login")

# ------------------ DASHBOARD VIEWS ------------------
@login_required
def student_dashboard(request):
    return render(request, "index.html")

@login_required
def teacher_dashboard(request): 
    return render(request, "teacher/teacher_dashboard.html")

@login_required
def admin_dashboard(request):
    return render(request, "index.html")

#--------------- View all courses ---------------
def course_list(request):
    all_course= Course.objects.all()
    return render(request, 'teacher/course_list.html', {'course': all_course})

#--------------- add a new course ---------------
def add_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        instructor = request.POST.get('instructor')

        if title and description and instructor:
            Course.objects.create(title=title, description=description, instructor=instructor)
            messages.success(request, "Course added successfully!")
            return redirect('course_list')
        else:
            messages.error(request, "Please fill all fields.")

    return render(request, 'teacher/add_course.html')

 #--------------- edit course --------------- 
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        instructor = request.POST.get('instructor')

        if title and description and instructor:
            course.title = title
            course.description = description
            course.instructor = instructor
            course.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')
        else:
            messages.error(request, "Please fill all fields.")

    return render(request, 'teacher/edit_course.html', {'course': course})

#--------------- view detail course --------------- 
def course_detail(request,id):
    one_course = get_object_or_404(Course, id=id)
    return render(request,'teacher/course_detail.html',{'d':one_course})

 #--------------- delete course --------------- 
def delete_course(request,id):
    dc = Course.objects.get(id=id)
    dc.delete()
    return redirect('course_list')
