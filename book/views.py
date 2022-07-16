from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.
class ListBookView(ListView):
    template_name = "book/book_list.html"
    model = Book
