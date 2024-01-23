from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse


def student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Saved Successfully!')
    template = 'app1/student_form.html'
    context = {"form": form}
    return render(request, template, context)

def display_view(request):
    template = 'app1/display_student.html'
    data = Student.objects.all()
    context = {"data": data}
    return render(request, template, context)


