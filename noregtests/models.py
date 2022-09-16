from django.db import models

class Task(models.Model):
	description = models.CharField(max_length=512)

# class Step(models.Model):
# 	task = models.ForeignKey(Task, related_name='steps', on_delete=models.CASCADE)
# 	order = models.IntegerField(default=1)

# Create your models here.
class TestStep(models.Model):
	task = models.ForeignKey(Task, related_name='steps', on_delete=models.CASCADE)
	order = models.IntegerField(default=1)

class NonRegTest(models.Model):
	title = models.CharField(max_length=350)
	description = models.CharField(max_length=350)
	complete = models.BooleanField(default=False)
	steps = models.ManyToManyField(TestStep, related_name="noregtests")

	def __str__(self):
		return self.title