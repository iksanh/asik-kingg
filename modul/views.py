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

def forbidden(request, exception):
    return render(request, 'forbidden.html', status=403)



# Custom View

# Custom View 404 


def error_404(req, exception):
    return render(req, 'custom/404.html')

# def server_error(req, exception):
#     return render(req, 'custom/404.html', status=500)

def portal(request):
    return render(request, 'index.html', {} )