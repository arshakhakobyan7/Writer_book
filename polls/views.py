from .models import Writer, Book, CommentBook
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentBookForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('polls:login')
    else:
        form = UserForm()

    context = {
        'form': form,
    }
    return render(request, 'polls/register.html', context)

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
    form = CommentBookForm()
    return render(request, 'polls/book_details.html', {'book': book, 'comment': comment, 'form': form})


def add_comment(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    error = ''

    if request.method == "POST":
        form = CommentBookForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('polls:book_details', book_id=book_id)
        else:
            error = 'Form was incorrect.'
    else:
        form = CommentBookForm()

    context = {
        'form': form,
        'error': error,
        'book': book,
        'comment': CommentBook.objects.filter(book=book)
    }
    return render(request, 'polls/book_details.html', context)


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


def login_user(request):
    error = ''

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        userr = authenticate(request, username=username, password=password)

        if userr is not None:
            login(request, userr)
            return redirect('polls:writer')
        else:
            error = 'Invalid username or password'

    return render(request, 'polls/login.html', {'error': error})


def logout_user(request):
    logout(request)
    return render(request, 'polls/writer.html')

@login_required(login_url='polls:login_user')
def user(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'polls/user.html', {'user': user})
