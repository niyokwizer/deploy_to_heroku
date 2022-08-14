from django.urls import path
from . import views

urlpatterns = [
    
    
    path('',views.base, name='base'),
    path('home',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('add_movies/',views.add_movies,name='add_movies'),
    path('members/add_movies_record/',views.add_movies_record,name='add_movies_record'),


    #path('', views.home, name='home'),
    #path('register/', views.register, name='register'),
   
    path('user/login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('add_movies/',views.add_movies,name='add_movies'),
    path('add_movies/add_movies_record/',views.add_movies_record,name='add_movies_record'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'), 
    path('contact/',views.contact,name='contact'),
    path('about/',views.about, name='about'),
    path('news/',views.news,name='news'),
    path('add_movies/search/',views.search,name='search'),
]