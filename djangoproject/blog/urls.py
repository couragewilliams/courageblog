from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('create/post/',views.createpost, name='create'),
    path('update/post/<str:pk>/',views.updatepost, name='update'),
    path('delete/post/<str:pk>/',views.deletepost, name='delete'),
    path('single/<str:pk>/',views.single, name='single'),
    
]