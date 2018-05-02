from django import forms
#Import models
from .models import Todo

#Create form from model, use widget to apply HTML/CSS attributes
class NewTodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = ['text']
		widgets = {
			'text' : forms.TextInput(
			attrs={'class' : 'form-control', 'placeholder' : 'Enter task e.g. Defeat Voldemort', 
			'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'})
		}
