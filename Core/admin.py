from django.contrib import admin
from .models import *


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(Genre)

admin.site.register([Author, Book, Genre])
