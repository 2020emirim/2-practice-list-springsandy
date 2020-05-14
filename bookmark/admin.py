from django.contrib import admin

from bookmark.models import Bookmark

admin.sites.register(Bookmark)