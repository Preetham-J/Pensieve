from django.db import models

#Create database schema
class Todo(models.Model):
	text = models.CharField(max_length=100) #Text field for entering tasks
	complete = models.BooleanField(default=False) #Completed boolean

	def __str__(self):
		return self.text
