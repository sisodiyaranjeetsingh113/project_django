
from django.shortcuts import render,redirect
from .forms import TaskForm,TileForm,StatusForm
from .models import Task,Tile,Status
# Create your views here.
def homeview(request):
    obj1=Status.objects.all()
    obj2=Tile.objects.all()
    obj=Task.objects.all()
    return render(request,'index.html',{'obj':obj,'obj1':obj1,'obj2':obj2})
def createviewfortask(request):
    if request.method =="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            print("done")
            form.save()
            return redirect('add/')
    else:
        form=TaskForm()
        return render(request,'add1.html',{'form':form})
def createview(request):
    if request.method =="POST":
        form=TileForm(request.POST)
        if form.is_valid():
            print("done")
            form.save()
            return redirect('/')
    else:
        form=TileForm()
        return render(request,'add.html',{'form':form})
def updateview(request,id):
    if request.method =="POST":
        obj=Tile.objects.get(pk=id)
        form=TileForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            print("done1")
            form.save()
            return redirect('/')
    else:
        obj=Tile.objects.get(pk=id)
        form=TileForm(request.POST or None,instance=obj)
        return render(request,'update.html',{'form':form})


def deleteview(request,id):
    obj=Tile.objects.get(pk=id)
    obj.delete()
    return redirect('/')


