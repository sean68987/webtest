from django.urls import path
from . import views 
urlpatterns =[
    path('hello/',views.say_hello),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload/success/', views.upload_success, name='upload_success'),
]