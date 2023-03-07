from django.shortcuts import render , redirect
from django.http import HttpResponse
from . import models
from .forms import categoryForm

def index(request):
    return HttpResponse("Hello this is index page")

class CategoryController:
    def index(request):
        querySet = models.Category.objects.all()
        return render( request , 'category_index.html' , {"categories" : querySet[:]})
    
    def view(request , pk):
        queryset = models.Category.objects.get(pk = pk)
        return render(request ,'category_list.html', {'category' : queryset})
    
    def create(request):
        
        if request.method == "POST":
            form = categoryForm.CategoryForm(request.POST)
            if form.is_valid():
                category = form.save()
                return redirect('category_detail' , pk = category.id)
        else:
            form = categoryForm.CategoryForm()
        return render(request, 'category_create.html', {'form' : form})
    
    def delete(request , id):
        return HttpResponse(id) 