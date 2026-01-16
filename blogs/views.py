from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from testapp.models import About
from .models import Category,Blog,Comment
from django.db.models import Q
from Syntax.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def Home(request):
    featured_posts=Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=True,status='Published')
    # Fetching about us 
    try:
        about = About.objects.get()
    except:
        about = None
    context={
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)


# view function for category
def posts_by_category(request,category_id):
    # Fetch the post that belongs to the category with the id category_id
    posts = Blog.objects.filter(status="Published",category=category_id)
    # Use try/except when we want to do some custom action if the category does not exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        #  redirect the user to home page 
        return redirect ('home')
    #  use get_object_or_404 whe you when you want to show 404 error page if the category does not exists
    # category = get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        "category":category
    }
    return render(request,'posts_by_category.html',context)


# view function for individual blog  
def blogs (request,slug):
    single_blog = get_object_or_404(Blog,slug=slug, status = "Published")
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info) # for redirecting to same page after adding comment 
        
    # Comments 
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    context={
        "single_blog":single_blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request, 'blogs.html',context)


# view function for search
def search(request):
    keyword = request.GET.get('keyword')
    print("keyword==",keyword)
    
    blogs=Blog.objects.filter(Q(title__icontains =keyword) | Q(short_description__icontains= keyword) | Q(blog_body__icontains=keyword),status="Published")
    context={
        'blogs':blogs,
        'keyword':keyword,
    }
    print(blogs)
    return render(request,'search.html',context)
    

# view function for register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('register')
        else:
            print(form.errors)
    else :
        form = RegistrationForm()
    context={
        'form':form,
    }
    return render (request,'register.html',context)

#  view function for login 
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect ('dashboard') 
        
    form = AuthenticationForm()
    context={
        'form':form,
        
    }
    return render (request, 'login.html',context)


# View function for logout
def logout(request):
    auth.logout(request)
    return redirect ('home')
    