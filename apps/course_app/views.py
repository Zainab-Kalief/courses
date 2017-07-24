from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)

def addCourse(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def removeButton(request, id):
    context = {
        'delete_course': Course.objects.get(id=id)
    }
    return render(request, 'course_app/remove.html', context)

def destroy(request, id):

    if request.POST['action'] == "yes":
        delete_course = Course.objects.get(id=id)
        delete_course.delete()
        return redirect('/')
    elif request.POST['action'] == "no":
        return redirect('/')
