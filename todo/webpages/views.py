from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def home(request):
    todo=Todo.objects.order_by('-created_date')
    data={
        'todo':todo,
    }
    return render(request, 'webpages/home.html',data)

def create(request):
    title=''
    desc=''
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        todo=Todo(title=title,description=desc)
        todo.save()
        return redirect('home')
    return render(request, 'webpages/createTodo.html')

def delete(request, id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')

def read(request,id):
    todo=Todo.objects.get(id=id)
    data={
        'todo':todo,
    } 
    return render(request, 'webpages/todoDetails.html',data)

def edit(request,id):
    todo=Todo.objects.get(id=id)
    data={
        'todo':todo,
    }
    if request.method=="POST":
        todo.title=request.POST['title']
        todo.description=request.POST['desc']
        todo.save()
        return redirect('home')
    return render(request, 'webpages/editTodo.html',data)