from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from cbvApp.models import Course
from django.urls import reverse_lazy

# Create your views here.
class CourseListView(ListView):
    model = Course
    # defaulttemplate_name = 'course_detail.html'
    #default context_object_name = 'course_list.html'

class CourseDetailView(DetailView):
    model = Course
    # defaulttemplate_name = 'course_detail.html'
    #default context_object_name = 'course_list.html'

class CourseCreateView(CreateView):
    model = Course
    fields = ['course_name','course_price','course_description','course_instructor','course_rating']
    success_url = reverse_lazy('courses')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['course_name','course_price','course_description','course_instructor','course_rating']
    success_url = reverse_lazy('courses')

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses')
    