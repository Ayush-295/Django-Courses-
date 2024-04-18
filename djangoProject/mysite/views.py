from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegistrationForm
import json


def index(request):
    return render(request, "mysite/index.html")


def courses(request):
    course_list = Course.objects.all()
    context = {
        "courses": course_list
    }

    return render(request, "mysite/courses.html", context)


def blog(request):
    return render(request, "mysite/blog.html")


def pricing(request):
    return render(request, "mysite/pricing.html")


def testimonials(request):
    return render(request, "mysite/testimonials.html")


def optin(request):
    if request.method == "POST":
        name = request.POST.get("name")
        country = request.POST.get("country")
        email = request.POST.get("email")
        info = Person(name=name, country=country, email=email)
        info.save()
        opt = True
        context = {"optedin": opt}
        print(name, country, email)
        return render(request, "mysite/optin.html", context)
    else:
        return render(request, "mysite/optin.html")


def course_detail(request, num):
    course = Course.objects.get(id=num)
    sections = Section.objects.filter(course=course)

    lessons = Lesson.objects.filter(lesson=course)
    context = {
        "course_id": num,
        'course': course,
        "lesson": lessons,
        "sections": sections
    }
    return render(request, "mysite/course_details.html", context)


def lesson_detail(request, num, num1):
    course = Course.objects.get(id=num)
    sections = Section.objects.filter(course=course)

    lessons = Lesson.objects.filter(lesson=course)
    lesson = Lesson.objects.get(id=num1)
    context = {
        'current_lesson': lesson,
        'course': course,
        "lesson": lessons,
        "sections": sections

    }
    return render(request, "mysite/lesson_detail.html", context)


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            return redirect('blog')
        else:
            errors = form.errors.as_json()
            form = UserRegistrationForm()
            parsed_json = json.loads(errors)

            context = {
                'form': form,
                'errors': errors
            }
            return render(request, 'mysite/signup.html', context)

    else:
        form = UserRegistrationForm()
        context = {
            "form": form
        }
        return render(request, "mysite/signup.html", context)
