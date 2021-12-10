from django.db import models

# Create your models here.
class Status(models.Model):
    status=models.CharField(max_length=50)
    def __str__(self):
        return self.status

class Task(models.Model):
    title=models.CharField(max_length=50,unique=True)
    order=models.CharField(max_length=60)
    description=models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    assigned_user=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Tile(models.Model):
    launch_date=models.DateField()
    status=models.OneToOneField(Status,on_delete=models.CASCADE)
    task=models.ManyToManyField(Task)
    def __str__(self):
        return self.launch_date
