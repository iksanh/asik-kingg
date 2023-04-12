from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    context = {
        'post' : 'coba',
        'title' : 'title'
    }

    return render(request, 'dashboard.html', context)

def forbidden(request, exception):
    return render(request, 'forbidden.html', status=403)
