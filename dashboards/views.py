from django.shortcuts import redirect, render
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from dashboards.forms import CategoryForm

# view function for dashboard
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)

# view function for categories
def categories(request):
    return render (request, 'dashboard/categories.html')
    
# view function for adding new categories
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context={
        'form':form
    }
    return render (request,'dashboard/add_category.html', context)
    