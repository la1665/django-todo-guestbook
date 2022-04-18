from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
import datetime

from .models import Todo
from .forms import TodoForm, NewTOdoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    newform = NewTOdoForm()

    mydate = datetime.datetime.now()

    context = {'todo_list': todo_list,
                'form': newform,
                'mydate': mydate
    }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    newform = NewTOdoForm(request.POST)

    if newform.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        new_todo = newform.save()
        
    return redirect('todo-index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('todo-index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('todo-index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('todo-index')