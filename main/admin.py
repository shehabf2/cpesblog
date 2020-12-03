from django.contrib import admin
from . models import * #instead of * we can use Post but * is for all

# Register your models here.
admin.site.register(Post)
#admin.site.register(Author)
