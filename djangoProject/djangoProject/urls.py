from django.contrib import admin
from django.urls import path, include
from mysite import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("courses/", views.courses, name="courses"),
    path("blog/", views.blog, name="blog"),
    path("optin/", views.optin, name="optin"),
    path("pricing/", views.pricing, name="pricing"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("courses/<int:num>/", views.course_detail, name="details"),
    path("courses/<int:num>/<int:num1>", views.lesson_detail, name="lesson_detail"),
    path("signup/", views.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='./registration/login.html'), name="login"),

]
