from django.contrib import admin
from .models import Post, Board, Issue, Item

# Register your models here.
admin.site.register(Post)

admin.site.register(Board)

admin.site.register(Issue)

admin.site.register(Item)