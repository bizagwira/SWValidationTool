from django.urls import path
from .views import tests, tasks, steps



urlpatterns = [
	path('', tests.index, name="index"),
	path('add', tests.add, name="add"),
	path('test/delete/<int:test_id>/', tests.delete, name="testdelete"),
	path('test/edit/<int:test_id>/', tests.edit, name="testedit"),
	path('test/update/<int:test_id>/', tests.update, name="testupdate"),
	path('test/<int:test_id>/', tests.detail, name="test"),
	path('step/add/<int:test_id>/', steps.add, name="addstep"),
	path('task/all', tasks.showalltask, name="showalltask"),
	path('task/add', tasks.newtask, name="addnewtask"),
	path('task/delete/<int:test_id>/', tasks.delete, name="taskdelete"),
	# path('task/edit/<int:test_id>/', tasks.newtask, name="taskedit"),
 #   	path('success/', tests.success, name='success')
]