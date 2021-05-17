from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article, Comment
from article.forms import ArticleForm, SearchForm
from django.core import serializers
from django.http import JsonResponse



class LikeAdd(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        user = self.request.user
        if user in article.likes.all():
            raise ValueError("Лайк Уже был поставлен")
        else :
            article.likes.add(user)
            article.save()
        return JsonResponse({"data": "www"})

class LikeDelete(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        user = self.request.user
        article.likes.remove(user)
        article.save()
        return JsonResponse({"data": "www"})

class LikeAddComment(View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        user = self.request.user
        comment.likes.add(user)
        comment.save()
        return JsonResponse({"data": "www"})

class LikeDeleteComment(View):
    def get(self, requset, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        user = self.request.user
        comment.likes.remove(user)
        comment.save()
        return JsonResponse({"data": "www"})