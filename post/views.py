from django.shortcuts import render
from django.core.paginator import Paginator

# Models
from .models import Post


def posts(req, page_number):
    pages = Paginator(Post.objects.all(), 10)

    try:
        page_number = int(page_number)
        if pages.num_pages >= page_number:
            return render(req, 'posts.html', { 'posts': pages.page(page_number) })
        else:
            return render(req, '404.html')
    except:
        return render(req, '404.html')
