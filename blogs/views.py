from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Blog


def Home(request):
    categories = Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=True,status='Published')
    print(posts)
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
    }
    return render(request,'home.html',context)



def posts_by_category(request,category_id):
    # Fetch the post that belongs to the category with the id category_id
    posts = Blog.objects.filter(status="Published",category=category_id)
    context={
        'posts':posts
    }
    return render(request,'posts_by_category.html',context)
