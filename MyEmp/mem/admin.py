from django.contrib import admin
from .models import Contact, Department,Role,Employee

# Register your models here.
admin.site.register(Department),
admin.site.register(Role),
admin.site.register(Employee),
admin.site.register(Contact),