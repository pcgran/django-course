from django.db import models

# Create your models here.

class ChoreList(models.Model):
	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()

	#define el comportamiento que va a tener un objeto de este tipo al intentar imporimirlo por pantalla
	def __str__(self):
		return self.name

class Chore(models.Model):
	chore_list = models.ForeignKey(ChoreList)
	name = models.CharField(max_length=100)
	due_date = models.DateTimeField()
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.name