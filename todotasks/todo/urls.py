from django.urls import path
from .views import CreateTodo, GetAllTodos, Updatetodo, DeleteTodo
urlpatterns = [
    path(r'create/', CreateTodo.as_view(), name='createTodo'),
    path(r'getall/', GetAllTodos.as_view(), name='createTodo'),
    path(r'update/', Updatetodo.as_view(), name='createTodo'),
    path(r'delete/', DeleteTodo.as_view(), name='createTodo'),

]