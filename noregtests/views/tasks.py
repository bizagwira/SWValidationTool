from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


from noregtests.models import Task



def showalltask(request):
	tasks = Task.objects.all()
	return render(request, 'task/all.html', {'tasks': tasks})

def newtask(request):
	tasks = Task.objects.all()
	return render(request, 'task/add.html', {'tasks': tasks})

@require_http_methods([ "POST"])
def add(request):
	description = request.POST.get('description', '')
	task = Task(description=description)
	task.save()
	return redirect(request.META['HTTP_REFERER'])

def edit(request, test_id):
	try:
		task = Task.objects.get(id = test_id)
		return render(request, 'task/edit.html', {'task': task})
	except Exception as e:
		print(f"Test doesn't exists {e.args}")
	return redirect(request.META['HTTP_REFERER'])

def delete(request, test_id):
	try:
		record = Task.objects.get(id = test_id)
		record.delete()
		print("Record deleted successfully!")
	except:
		print("Record doesn't exists")
	return redirect('showalltask')
	