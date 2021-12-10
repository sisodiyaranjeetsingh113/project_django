from django.contrib import admin
from .models import Task,Tile,Status
# Register your models here.
admin.site.register(Task)
admin.site.register(Tile)
admin.site.register(Status)