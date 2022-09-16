from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


from noregtests.models import NonRegTest

def index(request):
	tests = NonRegTest.objects.all()
	return render(request, 'tests/index.html', {'tests': tests})

@require_http_methods([ "POST"])
def add(request):
	title = request.POST.get('title', '')
	description = request.POST.get('description', '')
	test = NonRegTest(title=title, description=description)
	test.save()
	return redirect('/')


def edit(request, test_id):
	try:
		test = NonRegTest.objects.get(id = test_id)
		return render(request, 'tests/edit.html', {'test': test})
	except Exception as e:
		print(f"Test doesn't exists {e.args}")
	return redirect(request.META['HTTP_REFERER'])

@require_http_methods([ "POST"])
def update(request, test_id):
	try:
		test = NonRegTest.objects.get(id = test_id)
		test.title = request.POST.get('title', '')
		test.description = request.POST.get('description', '')
		test.save()
		return redirect('/')
	except Exception as e:
		print(f"Test doesn't exists {e.args}")
	return redirect(request.META['HTTP_REFERER'])


def delete(request, test_id):
	try:
		record = NonRegTest.objects.get(id = test_id)
		record.delete()
		print("Record deleted successfully!")
	except:
		print("Record doesn't exists")
	return redirect('/')

def detail(request, test_id):
	record = NonRegTest
	try:
		test = NonRegTest.objects.get(id = test_id)
		steps = test.steps.all()
		return render(request, 'tests/detail.html', {'test': test, 'steps': steps})
	except Exception as e:
		print(f"Test doesn't exists {e.args}")
	return redirect(request.META['HTTP_REFERER'])
