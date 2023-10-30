from django.contrib import admin
from .models import Writer, Book, CommentBook

admin.site.register(Writer)
admin.site.register(Book)
admin.site.register(CommentBook)