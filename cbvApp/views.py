from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvApp.models import Course
from django.urls import reverse_lazy

# Create your views here.
class CourseListView(ListView):
    model = Course
    #defaulttemplate_name = 'course_detail.html'
    #default context_object_name = 'course_list.html'