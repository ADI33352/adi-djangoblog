from django.db.models import Count
from django.shortcuts import render
from .models import Blog 
from .models import Guest
from .models import Index
from .models import Category
from .models import ContactForm
from .models import singleblog,author
# Create your views here.
def get_category_count():
    queryset = singleblog \
         .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

def index(request):
    category_count = get_category_count()
    query = Index.objects.all()
    context = {'query':query,'category_count':category_count}
    return render(request,'index.html',context)
def about(request):
    comment = Guest.objects.all()
    context = {'comment':  comment}
    return render(request,'about.html',context)
def blog(request):
    
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request,'blog.html',context)
def blogsingle(request):
    category_count = get_category_count()
    posts = singleblog.objects.all()
    context = {'posts':posts,
    'category_count':category_count}
    return render(request,'blogsingle.html',context)
def contact(request):
    formclass = ContactForm

    return render(request, 'contact.html', {
        'form': formclass })