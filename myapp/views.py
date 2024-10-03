from .models import MyModel
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def create1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        MyModel.objects.create(name=name, description=description)
        return HttpResponse("Record created successfully")
    return render(request, 'create.html')

def read(request):
    objects = MyModel.objects.all()
    return render(request, 'read.html', {'objects': objects})

def update(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        instance.name = name
        instance.description = description
        instance.save()
        return HttpResponse("Record updated successfully")
    return render(request, 'update.html', {'instance': instance})

def delete(request, pk):
    instance = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return HttpResponse("Record deleted successfully")
    return render(request, 'delete.html', {'instance': instance})
