from django.contrib import admin

# Register your models here.

from .models import Managers,Employee,Admin

admin.site.register(Employee)
admin.site.register(Managers)
admin.site.register(Admin)