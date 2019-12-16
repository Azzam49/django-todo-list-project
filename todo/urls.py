from django.urls import path
from . import views

urlpatterns = [
    path('',views.todoView, name="todo-page"),
    path('addTodo/',views.addTodoView),
    path('deleteTodo/<int:todo_id>/',views.deleteTodo), #<int:todo_id> this will match any integer and names it todo_id

    # our deleteTodo view does an action on the database and redirects us back to the pervious url
]