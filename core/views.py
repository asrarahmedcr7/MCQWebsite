from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

def teacher_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_teacher:
            login(request, user)
            return redirect('Teacher:home')
        else:
            return render(request, 'core/teacher_login.html', {'error':'Invalid Credentials'})
    return render(request, 'core/teacher_login.html')

def student_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_teacher:
            login(request, user)
            return redirect('Student:index')
        else:
            return render(request, 'student_login.html', {'error':'Invalid Credentials'})
    return render(request, 'core/student_login.html')

def homeview(request):
    return render(request, 'core/main_homepage.html')

class CoreLogoutView(LogoutView):
    next_page = reverse_lazy('core:home')