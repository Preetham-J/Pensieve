from django import forms

#Main form for user, indicates max. length of task and form attributes in HTML
class TodoForm(forms.Form):
	text = forms.CharField(max_length=100,
		#Pass HTML and CSS attributes to field 
		widget=forms.TextInput(
			attrs={'class' : 'form-control', 
			'placeholder' : 'Enter task e.g. Defeat Voldemort', 
			'aria-label' : 'Todo', 
			'aria-describedby' : 'add-btn'}))