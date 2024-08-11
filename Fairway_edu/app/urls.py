"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.quickstart.views import index,sign_up,login_view,course_list,dashboard,course_create,delete_course,abc
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
      path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', sign_up, name='sign_up'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('course/course_list/', course_list, name='course_list'),
    path('course/course_form/', course_create, name='course_create'),
    path('course/abc/', abc, name='abc'),
    path('course/course_delete/<int:id>/', delete_course, name='delete_course'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
