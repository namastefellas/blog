from django.http import response
from django.http.response import JsonResponse, Response
from hello.article.models import Article
from django.views import APIView
from article.models import Article
from api.serializers.article import ArticleSerializer
from django.shortcuts import reverse, get_object_or_404

import json


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serialezer = ArticleSerializer(articles, many=True)
        response_data = serialezer.data
        return Response(data=response_data)


    def post(self, request, *args, **kwargs):
        article_data = request.data
        serializer = ArticleSerializer(data=article_data)
        is_valid = serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return JsonResponse({'id': article.id})

class ArticleDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(article)
        response_data = serializer.data
        return Response(response_data)




class ArticleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            article = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class ArticleUpdateView(APIView):
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response(serializer.data)

class ArticleDeleteView(APIView):
    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response(status=204)