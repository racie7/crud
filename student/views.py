from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.db.models import Q


def students_list(request):
    # students = Student.objects.all()

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    students = Student.objects.filter(
        Q(stud_name__icontains=search_query) | 
        Q(stud_course__icontains=search_query) |
        Q(stud_stud_id__icontains=search_query)
    )

    context = {
        'students': students,
        'search_query': search_query,
    }
    return render(request, 'student/list.html', context)


def create_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students-list')

    context = {
        'form': form,
    }
    return render(request, 'student/create.html', context)


def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students-list')

    context = {
        'student': 'student',
        'form': form,
    }
    return render(request, 'student/edit.html', context)


def delete_student(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('students-list')

    context = {
        'student': student,
    }
    return render(request, 'student/delete.html', context)
