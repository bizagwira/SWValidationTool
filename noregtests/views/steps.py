from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


from noregtests.models import NonRegTest, TestStep, Task



@require_http_methods([ "POST"])
def add(request, test_id):
	try:
		description = request.POST.get('description', '')
		task = Task(description=description)
		task.save()
		step = TestStep(task=task, order=2)
		step.save()
		test = NonRegTest.objects.get(id = test_id)
		test.steps.add(step)
		test.save()
		print("Record deleted successfully!")
	except Exception as e:
		print(f"Test id: {test_id} Record doesn't exists {e.args}")
	return redirect(request.META['HTTP_REFERER'])