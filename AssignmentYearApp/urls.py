"""
URL configuration for TeachingManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.shortcuts import redirect
from .import views

urlpatterns = [
    #For the COURSES
    path('section-courses/', views.section_courses_list, name='section_courses_list'),
    path('section-courses/show/<int:idCourseYear>/', views.courseyear_show, name='courseyear_show'),

        #For updating only the comment in a CourseYear
    path('update-course-year-comment/<int:idCourseYear>/', views.update_course_year_comment, name='update_course_year_comment'),
        #modifyning the points of a professor Assigned in a Course Year
    path('update-assignment/<int:idAssignment>/', views.update_assignment, name='update_assignment'),
        #assigning a new professor in the CoureYear
    path('assign_professor/<int:professor_id>/<int:course_year_id>/', views.assign_professor, name='assign_professor'),
        #deleting the assign points of one professor in one Course
    path('delete_professor/<int:idProfessor>/<int:idCourseYear>/', views.delete_courseyear_professor, name='delete_courseyear_professor'),

    #For DUPLICATING   
        #for selecting original year - selected year
    path('select-years/', views.select_years_for_duplication, name='select_years'),
        #for making the duplication
    path('course/duplicate/<int:idCourseYear>/', views.duplicate_course_assignment, name='duplicate_course_assignment'),

    #For the PROFESSORS
    path('section-professors/', views.section_professors_list, name='section_professors_list'),

]
