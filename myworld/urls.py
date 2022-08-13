"""myworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a UR L to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as auth_views
#from members import views as user_views
#from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('members.urls')),

    #path('', user_views.home, name='home'),
    #path('register/', user_views.register, name='register'),
   
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('add_movies/',user_views.add_movies,name='add_movies'),
    #path('add_movies/add_movies_record/',user_views.add_movies_record,name='add_movies_record'),
    #path('update/<int:id>', user_views.update, name='update'),
    #path('update/updaterecord/<int:id>', user_views.updaterecord, name='updaterecord'), 
]

if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
