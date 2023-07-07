from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseNotFound

# Create your views here.

@login_required
def index(request):
    context = {
        'post': 'coba',
        'title': 'title',
        'dashboard': True
    }

    return render(request, 'dashboard.html', context)

def error_403(request, exception):
    return render(request, 'custom/403.html')


def error_404(req, exception):
    return render(req, 'custom/404.html')

def error_500(req, exception):
    return render(req, 'custom/500.html')

def portal(request):
    return render(request, 'index.html', {} )