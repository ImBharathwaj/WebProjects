from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Dhanasekar',
        'title': 'Blog Post 1',
        'content': 'Blog post content',
        'date_posted': 'August 27, 2018'
    },

    {
        'author': 'Sarathbabu',
        'title': 'Blog Post 2',
        'content': 'Blog post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(req):
    context = {
        'posts': posts
    }
    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, 'blog/about.html', {'title': 'Nothing'})
