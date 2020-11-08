from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Category(models.Model):
  title = models.CharField(max_length=100)
  def __str__(self):
        return self.title
class author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default= True)
    def __str__(self):
        return self.user.username



class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to ='images', default ="")
    timestames = models.DateTimeField(auto_now_add=True,null=True)

class Guest(models.Model):
    content = models.TextField()
    imagee = models.ImageField(upload_to ='images', default = '')
    name = models.CharField(max_length=20)
    postion = models.CharField(max_length=20)

class Index(models.Model):
    categoriess = models.OneToOneField(Category,on_delete = models.CASCADE, null= True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to = 'thumbnails',default = '')
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class ContactForm(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField()
    message =models.CharField(max_length=300)

    def __str__(self):
        return self.name
class singleblog(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    images = models.ImageField(upload_to = 'imagess',default = '')
    description = models.TextField()
    viewcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    timestamps = models.DateField(auto_now_add=True)
    author = models.ForeignKey(author,on_delete= models.CASCADE)
    categories = models.OneToOneField(Category,on_delete = models.CASCADE, null= True)
