from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Publisher, Book, Comment


class HomeView(TemplateView):
    template_name = 'vote/index.html'


class PublisherListView(ListView):
    model = Publisher
    template_name = 'vote/publisher.html'
    context_object_name = 'objects'
    ordering = 'name'


class PublisherCreateView(CreateView):
    model = Publisher
    fields = '__all__'
    template_name = 'vote/add.html'


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'vote/publisher_detail.html'


class BookListView(ListView):
    model = Book
    template_name = 'vote/books.html'
    context_object_name = 'books'


class BooksCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'vote/add.html'


class CommentCreateView(CreateView):
    model = Comment
    fields = '__all__'
    template_name = 'vote/add.html'


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'vote/books.html'
