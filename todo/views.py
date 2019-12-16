from django.shortcuts import render , redirect
from .models import TodoModel
from django.http import HttpResponseRedirect

# Create your views here.
def todoView(request):
    context = {
        "todo_items":TodoModel.objects.all()
    }
    return render(request,"todo.html",context)


def addTodoView(request):
    c = request.POST["content"]
    new_item = TodoModel(content = c)
    new_item.save()
    return  redirect("/todo")
    #return HttpResponseRedirect("/todo/")

def deleteTodo(request , todo_id): #todo_id arugment is the integer passed on the url
    item_to_delete = TodoModel.objects.get( id = todo_id )
    item_to_delete.delete()

    return redirect('/todo')