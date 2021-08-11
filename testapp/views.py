from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from .models import Student
from .forms import studentUpdateForm
# Create your views here.

def home(request):
    template = 'testapp/home.html'
    cursor = connection.cursor()
    all_student_data = cursor.execute(" SELECT * FROM STUDENT ")
    rows = cursor.fetchall()
    context = {'rows':list(rows)}
    return render(request,template,context)

def Create(request):
  
    form = studentUpdateForm()
    if request.method == "POST":
        f = studentUpdateForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, f'Created successfully !')
            return redirect('/')
    context = {'form':form}
    template = 'testapp/create.html'
    return render(request,template,context)

def Update(request, pk):
    ins = Student.objects.get(student_no = pk)
    form = studentUpdateForm(instance=ins)
    if request.method == "POST":
        f = studentUpdateForm(request.POST,instance=ins)
        if f.is_valid():
            f.save()
            messages.success(request, f'updated successfully !')
            return redirect('/')
    context = {'form':form}
    template = 'testapp/update.html'
    return render(request,template,context)

def Delete(request, pk):
    ins = Student.objects.get(student_no = pk)
    if request.method == "POST":
        ins.delete()
        messages.success(request, f'deleted successfully !')
        return redirect('/')
    context = {}
    template = 'testapp/delete.html'
    return render(request,template,context)