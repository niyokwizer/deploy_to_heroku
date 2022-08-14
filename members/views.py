from re import template
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import context , loader
from django import forms
from django.urls import path
from .models import movies


def base(request):
    return render(request, 'users/base.html')

def home(request):
  template=loader.get_template('users/home.html')
  movies_content= movies.objects.all().values()
  context= {
    'movies_content': movies_content,
  }
  return HttpResponse(template.render(context,request))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def add_movies(request):
  template = loader.get_template('add_movies.html')
  return HttpResponse(template.render({}, request))
       
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render({}, request))

def news(request):
  template = loader.get_template('news.html')
  return HttpResponse(template.render({}, request))


def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render({}, request))

def add_movies_record(request):
    title= request.POST['title']
    main_actor = request.POST['main_actor']
    genre= request.POST['genre']
    description_= request.POST['description']
    movies_= request.FILES.get('movies')
    #released_date = request.POST.get('released_date')
    #rreleased_date = request.POST['rreleased_date']
    #released_date = request.POST['released_date']
    #movies_=request.FILES[movies_]
    #thumbnail=request.FILES['thumbnail']
    url=request.POST['url']
    thumbnail= request.FILES.get('thumbnail')
    
    
    user_id= request.POST['user_id']
    

    nvideo = movies(title=title, main_actor=main_actor,genre=genre,descripltion=description_,thumbnail=thumbnail,video=movies_,url=url,user_id=user_id)
    nvideo.save()
    return HttpResponseRedirect(reverse('add_movies'))
 

def update(request, id):
  mymember = movies.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def search(request):
  title=request.POST['search']
  mysearch=movies.objects.filter(title__contains=title)
  template=loader.get_template('search.html')
  context = {
    'mysearch': mysearch,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    title= request.POST['title']
    main_actor = request.POST['main_actor']
    genre= request.POST['genre']
    description_= request.POST['description']
    movies_ = request.POST['video']
    url=request.POST['url']
    thumbnail= request.POST['thumbnail']
    #released_date_ = request.POST['released_date']
    member = movies.objects.get(id=id)
    member.title = title
    member.main_actor = main_actor
    member.genre = genre
    member.descripltion=description_
    member.video = movies_
    #member.released_date = released_date_
    
    member.thumbnail = thumbnail
    member.url=url
    member.save()
    return HttpResponseRedirect(reverse('home'))  

