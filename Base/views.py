from django.shortcuts import render, get_object_or_404

from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'Base/index.html', {'courses': courses})

def detail(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, 'Base/detail.html', {'course': course})