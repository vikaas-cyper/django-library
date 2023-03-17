from django.shortcuts import render , redirect
from django.http import HttpResponse
from . import models
from .forms import categoryForm

def index(request):
    return HttpResponse("Hello this is index page")

class CategoryController:
    def index(request):
        querySet = models.Category.objects.all().order_by('name')
        return render( request , 'category/index.html' , {"categories" : querySet[:]})
    
    def view(request , pk):
        queryset = models.Category.objects.get(pk = pk)
        return render(request ,'category/list.html', {'category' : queryset})
    
    def create(request):
        
        if request.method == "POST":
            form = categoryForm.CategoryForm(request.POST)
            if form.is_valid():
                category = form.save()
                return redirect('category_detail' , pk = category.id)
        else:
            form = categoryForm.CategoryForm()
        return render(request, 'category/create.html', {'form' : form})
    
    
    def edit(request, pk):
        category = models.Category.objects.get(pk = pk)
        form = categoryForm.CategoryForm(instance=category)
        if request.method == "POST":
            form = categoryForm.CategoryForm(request.POST , instance=category)
            if form.is_valid():
                form.save()
                return redirect('category_list')
        
        return render(request, 'category/edit.html', {'form' : form, 'category' : category })
    
        
        
    def delete(request , pk):
        category = models.Category.objects.get(pk = pk)
        if request.method == "POST":
            category.delete()
            return redirect('category_list')
        
        
        return render(request, 'category/delete.html', {'category' : category})
