from django import forms

from .models import Post, Board, Item, Issue

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'text',)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title', 'text',)

class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('title', 'text',)