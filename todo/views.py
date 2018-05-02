from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

#Import models and forms 
from .models import Todo
from .forms import TodoForm, NewTodoForm

#Main request (landing page)
def index(request):
	#Query tasks from database
	todo_list = Todo.objects.order_by('id')
	
	#Create form
	form = NewTodoForm()
	
	#Pass query to HTML and render
	context = {'todo_list' : todo_list, 'form' : form}
	return render(request, 'todo/index.html', context)

#Add task to list request (POST)
@require_POST
def addTodo(request):
	#Create form with POST
	form = NewTodoForm(request.POST)

	#Query count of tasks in database
	count = Todo.objects.all().count()
	
	#Max. 14 tasks that fit on page
	if form.is_valid() and count < 13:
		new_todo = form.save() #Send to database

	#Redirect to refresh page
	return redirect('index')

#Complete task request
def completeTodo(request, todo_id):
	#Get ID of task completed
	todo = Todo.objects.get(pk=todo_id)
	
	#Set task completed field to True
	todo.complete = True
	
	#Send to database
	todo.save()
	
	#Redirect to refresh page
	return redirect('index')

#Delete completed tasks request
def deleteCompleted(request):
	#Query for tasks with completed field = True 
	Todo.objects.filter(complete__exact=True).delete()
	
	#Redirect to refresh page
	return redirect('index')

#Delete all tasks request
def deleteAll(request):
	#Delete all tasks in database
	Todo.objects.all().delete()
	
	#Redirect to refresh page
	return redirect('index')