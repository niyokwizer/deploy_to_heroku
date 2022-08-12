import site
from django.contrib import admin
from .models import movies,user,Members

# Register your models here.

admin.site.register([user,movies,Members])
