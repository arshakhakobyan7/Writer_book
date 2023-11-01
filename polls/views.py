from .models import Writer, Book, CommentBook
from django.shortcuts import render, redirect
from django.http import HttpResponse


def writer(request):
    wrt = Writer.objects.all()
    context = {"wrt": wrt}
    return render(request, 'polls/writer.html', context)


def writer_books(request, writer_id):
    writer = Writer.objects.get(id=writer_id)
    books = Book.objects.filter(writer=writer)
    return render(request, 'polls/writer_books.html', {'writer': writer, 'books': books})



def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    comment = CommentBook.objects.filter(book=book)
    return render(request, 'polls/book_details.html', {'book': book, 'comment': comment})


def add_comment(request, book_id):
    if request.method == "POST":
        email = request.POST['email']
        text = request.POST['text']

        comment = CommentBook(book_id=book_id, email=email, text=text)
        comment.save()

        return redirect('polls:book_details', book_id=book_id)


def like(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        if subject == 'Like':
            book.like += 1
            book.save()
        elif subject == 'Dislike':
            book.dislike += 1
            book.save()


    return redirect('polls:book_details', book_id=book_id)