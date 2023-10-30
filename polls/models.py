from django.db import models


class Writer(models.Model):
    img = models.ImageField()
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Book(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    img = models.ImageField()
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class CommentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length=50)
    text = models.TextField('Text')

    def __str__(self):
        return f"Com:{self.book}-{self.email}"