from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path("", views.writer, name='writer'),
    path("<int:writer_id>/", views.writer_books, name='writer_books'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('add_comment/<int:book_id>/', views.add_comment, name='add_comment'),
    path('like/<int:book_id>/', views.like, name='like'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('<str:username>/', views.user, name='user'),
    path('logout/', views.logout_user, name='logout'),
]

