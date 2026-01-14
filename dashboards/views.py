from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from dashboards.forms import CategoryForm , BlogPostForm
from django.template.defaultfilters import slugify

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
    
# view function for for editing category
def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context={
        'form':form,
        'category':category,
    }
    return render (request,'dashboard/edit_category.html',context)   


# View function for delete category
def delete_category(request,pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect ('categories')



""" functions for blogs """
# view function for posts 
def posts(request):
    post=Blog.objects.all()
    context={
        'posts':post
    }
    return render(request,'dashboard/posts.html' , context)

# view function for adding new post
def add_post(request):
    if request.method =='POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False) # temporarily saving the form 
            post.author=request.user           
            post.save()
            title = form.cleaned_data['title']
            post.slug=slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            print("form is not valid")
            print(form.errors)
    form = BlogPostForm()
    context = {
            'form':form,
        }
    return render (request,'dashboard/add_post.html', context)