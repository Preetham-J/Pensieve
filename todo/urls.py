from django.urls import path

#Import views
from . import views

#Create url links
urlpatterns = [
    path('', views.index, name='index'), #Main link
    path('add', views.addTodo, name='add'), #Add task link
    path('complete/<todo_id>', views.completeTodo, name='complete'), #Completed task link
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'), #Delete completed tasks link
    path('deleteall', views.deleteAll, name='deleteall') #Delete all tasks link
]
