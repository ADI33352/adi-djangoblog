from django.urls import path
from blogs import views

urlpatterns = [

    path  ('', views.index ,name = 'index'),
    path ('about/', views.about, name = "about"),
    path  ("blog/", views.blog, name = "blog"),
    path  ("blogsingle", views.blogsingle, name = "blogsingle"),
    path  ("contact/", views.contact, name = "contact"),
]

