from django.shortcuts import render
from django.views.generic import View
from .models import *


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category_slug = kwargs.get('slug')
        category = Categories.objects.get(slug=category_slug)
        images = Images.objects.filter(category=category)
        context = {
            'images': images,
            'title': category.title
        }
        return render(request, 'category.html', context)
