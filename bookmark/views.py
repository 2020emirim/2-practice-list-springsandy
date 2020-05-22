from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from bookmark.models import Bookmark


class BookmarkList(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):    #bookmark_form.html
    model = Bookmark
    fields = ['site_name', 'url']    #<form>
    template_name_suffix = '_create'   #bookmark_create.html
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']    #<form>
    template_name_suffix = '_update'    #bookmark_update.html