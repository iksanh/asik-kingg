from django.shortcuts import render, get_object_or_404, redirect
from .forms import KasForm, Kas
from django.contrib.auth.decorators import permission_required
from modul.crud_params import CrudParams
# Create your views here.

paramater_kas = CrudParams('kas')
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
    context= paramater_kas.parameters(data=kas, kas=True, data_master=True) 
    return render(request, 'kas/list_kas.html', context)

def create_kas(request):
    form = KasForm()

    if request.method == 'GET':
        context = paramater_kas.parameters(form=form, modul=modul, action='Buat Data', kas=True, data_master=True)
        
        return render(request, crud['template']['create'], context)
    elif request.method == 'POST':
        form = KasForm(request.POST)
        context = paramater_kas.parameters(form=form, modul=modul, action='Buat Data', kas=True, data_master=True)
        
        if form.is_valid():
            form.save()
            return redirect('list-kas')
        else:
            return render(request, crud['template']['create'], context)

def edit_kas(request, id):

    form_id = get_object_or_404(Kas, id=id)

    if request.method =='GET':
        form = KasForm(instance=form_id)
        context = paramater_kas.parameters(kas=True, data_master=True, form=form, id=id, modul=modul, action='Edit Data') 
        return render(request, crud['template']['create'], context)
    elif request.method == 'POST':
        form =  KasForm(request.POST, instance=form_id)
        context = paramater_kas.parameters(form=form, modul=modul, action='Edit Data', kas=True, data_master=True)
        if form.is_valid():
            form.save()
            return redirect('list-kas')
        else:
            return render(request, crud['template']['create'], context)



def delete_kas(request, id):
    form_id = get_object_or_404(Kas, id=id)
    form_id.delete()
    return redirect('list-kas')

