from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'post' : 'coba',
        'title' : 'title'
    }

    return render(request, 'dashboard.html', context)

