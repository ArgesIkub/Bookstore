from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    memo = models.TextField(null=True)
    publisher = models.ForeignKey(to='Publisher', on_delete=DO_NOTHING) # Create foreign key
    author = models.ManyToManyField('Author') # Create a third table in a many-to-many relationship

    def __str__(self):
        return f"<Book object: {self.id} {self.title} >"

    __repr__ = __str__

class Publisher(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return "<Publisher object: {} {} >".format(self.id,self.name)

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "<Author object: {} {} >".format(self.id, self.name)

class Page(models.Model):
    number = models.PositiveIntegerField()
    book = models.ForeignKey(to=Book, on_delete=DO_NOTHING)

    def __str__(self):
        return f'{self.book.title} - {self.number}'