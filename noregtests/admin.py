from django.contrib import admin
from .models import NonRegTest, Task, TestStep

# Register your models here.
admin.site.register(NonRegTest)
admin.site.register(TestStep)
admin.site.register(Task)