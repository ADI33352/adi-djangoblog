from django.contrib import admin
from blogs.models import Blog
from blogs.models import Guest
from blogs.models import Index
from blogs.models import Category,author
from blogs.models import ContactForm
from blogs.models import singleblog
# Register your models here.
admin.site.register(Blog)
admin.site.register(Guest)
admin.site.register(Index)
admin.site.register(Category)
admin.site.register(ContactForm)
admin.site.register(singleblog)
admin.site.register(author)