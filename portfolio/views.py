from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, AllCarsForm, get_dynamic_form
from .models import ValetCars, get_model_by_name
import os

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def photography_home(request):
    img_folders = [
        os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'img', 'jpg', 'proj-1'), 
        os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'img', 'jpg', 'proj-2'), 
        os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'img', 'jpg', 'proj-3')
    ]
    
    images = []

    for folder in img_folders:
        folder_name = folder.split('/')[-1]  # Extract folder name (proj-1, proj-2, etc.)
        images += [f"img/jpg/{folder_name}/{file}" for file in os.listdir(folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

    print(images)
    
    return render(request, 'photography_home.html', {'photosArray': images})

def projects_home(request):
    return render(request, 'projects_home.html')

def add_car(request, model_name):
    ValetCarForm = get_dynamic_form(model_name)
    if request.method == 'POST':
        form = ValetCarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully!')
            return redirect('valet_system')
    else:
        form = ValetCarForm()
    
    return render(request, 'add_car.html', {'form': form, 'model_name': model_name})

def edit_car(request, model_name, guestID):
    model_class = get_model_by_name(model_name)
    model = model_class[0]
    if not model:
        return render(request, '404.html', status=404)
    
    car = get_object_or_404(model, guestID=guestID)
    DynamicCarForm = get_dynamic_form(model_name)

    if request.method == 'POST':
        form = DynamicCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('valet_system')
        
    else:
        form = DynamicCarForm(instance=car)

    return render(request, 'edit_car.html', {'form': form, 'car': car, 'model_name': model_name})

def delete_car(request, model_name, guestID):
    model_class = get_model_by_name(model_name)
    model = model_class[0]
    if not model:
        return render(request, '404.html', status=404)
    
    car = get_object_or_404(model, guestID=guestID)

    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car deleted successfully!')
        return redirect('valet_system')
    
    return render(request, 'confirm_delete.html', {'car': car})

def valet_system(request):
    car_list_db = ValetCars.objects.all()
    return render(request, 'valet_system.html', {'car_list_db': car_list_db})