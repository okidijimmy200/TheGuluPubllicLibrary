from django.shortcuts import render
from books.models import Book
from django.views import generic


# search bar
class SearchView(generic.ListView):
    template_name = 'search/views.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Book.objects.search(query)
        return Book.objects.all()
