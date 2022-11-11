from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from todoapp.forms import TodoForm
from todoapp.models import Todo


def home(request):
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')


    return render (request,"home.html",{'form':form,'todos':todos})

def update(request,Todo_id):
    todo = Todo.objects.get(id=Todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'update.html',{'form':form})

def delete(request,Todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=Todo_id).delete()
        return redirect("home")
    # return render(request,'home.html')