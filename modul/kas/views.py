from django.shortcuts import render, get_object_or_404, redirect
from .forms import KasForm, Kas
from django.contrib.auth.decorators import permission_required
# Create your views here.

modul = 'kas'
crud = {
    'template': {
        'create': 'kas/create_kas.html',
        'list': 'kas/list_kas.html'
    },
    'url': {
        'list': modul,
        'edit': 'edit-'+modul,
        'delete': 'delete-'+modul,
        'create': 'create-'+modul
    }
}
template_list = 'kas/list_kas.html'
template_create = 'kas/crate_kas.html'

permission_required('kas.view_kas')
def list_kas(request):

    kas = Kas.objects.all()
    context= {
        'data': kas,
        'link': crud["url"],
        'modul': modul
    }
    return render(request, crud['template']['list'], context)

def create_kas(request):

    form = KasForm()

    if request.method == 'GET':
        context = {
            'forms': form,
            'modul': modul,
            'action': 'Buat'

        }
        return render(request, crud['template']['create'], context)
    elif request.method == 'POST':
        form = KasForm(request.POST)
        context = {
            'forms': form,
            'modul': modul,
            'action': 'Buat'
        }
        if form.is_valid():
            form.save()
            return redirect('kas')
        else:
            return render(request, crud['template']['create'], context)

def edit_kas(request, id):

    form_id = get_object_or_404(Kas, id=id)

    if request.method =='GET':
        form = KasForm(instance=form_id)
        context = {
            'forms': form,
            'id': id,
            'modul': modul,
            'action': 'Edit'
        }
        return render(request, crud['template']['create'], context)
    elif request.method == 'POST':
        form =  KasForm(request.POST, instance=form_id)
        context = {
            'forms': form,
            'modul': modul,
            'action': 'Edit'
        }
        if form.is_valid():
            form.save()
            return redirect('kas')
        else:
            return render(request, crud['template']['create'], context)



def delete_kas(request, id):
    form_id = get_object_or_404(Kas, id=id)
    form_id.delete()
    return redirect('kas')

