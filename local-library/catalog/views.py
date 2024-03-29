from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book, Author, BookInstance, Genre


def index(request: HttpRequest) -> HttpResponse:
    
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_authors = Author.objects.count()
    
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    num_word_fiction_genre = Genre.objects.filter(name__exact = 'фантастика').count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_word_fiction_genre': num_word_fiction_genre,
        'num_visits': num_visits,
    }
    
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    
    model = Book


class AuthorListView(generic.ListView):
    
    model = Author
    paginate_by = 3

class AuthorDetailView(generic.DetailView):
    
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5
    
    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')