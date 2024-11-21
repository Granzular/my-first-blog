from . import views
from django.urls import path

app_name = "blog"

urlpatterns =[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('locations/',views.locations,name='locations'),
    path('contact/',views.contact,name='contact'),
    path('posts/<pk>/detail/',views.detail,name='detail'),
]
