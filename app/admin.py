from django.contrib import admin

from app.models import Author, Book, Page, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Page)