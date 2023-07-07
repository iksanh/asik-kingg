from django.shortcuts import render, get_object_or_404, redirect
from .forms import PinjamanForm, Pinjaman
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from modul.crud_params import CrudParams

pinjaman_param = CrudParams('pinjaman')



#add variable template
template_create = 'pinjaman/create_pinjaman.html'
template_list = 'pinjaman/list_pinjaman.html'
# Create your views here.



#function list pinjaman
# @permission_required('pinjaman.view_pinjaman')
def list_pinjaman(request):
    pinjaman  = Pinjaman.objects.all()
    context = pinjaman_param.parameters(data=pinjaman, data_master=True, pinjaman=True)
    return render(request, template_list, context)


@permission_required('pinjaman.add_pinjaman')
def create_pinjaman(request):
    #get form
    if request.method == 'GET':
        context = pinjaman_param.parameters(form=PinjamanForm(), data_master=True, pinjaman=True)
        
        return render(request, template_create, context)
    elif request.method == 'POST':
        form = PinjamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-pinjaman')
        else:
            return render(request, template_create, pinjaman_param.parameters(form=form, data_master=True, pinjaman=True))

def edit_pinjaman(request, id):
    
    form_id = get_object_or_404(Pinjaman, id=id)
    if request.method == 'GET':
        context = pinjaman_param.parameters(form=PinjamanForm(instance=form_id), id=id, data_master=True, pinjaman=True)
        # context = {
        #     'forms': PinjamanForm(instance=form_id),
        #     'id': id
        # }
        return render(request, template_create, context)
    elif request.method == 'POST':
        form = PinjamanForm(request.POST, instance= form_id)
        if form.is_valid():
            form.save()
            return redirect('list-pinjaman')
        else:
            return render(request, template_create, {'form': form_id})

def delete_pinjaman(request, id):
    pinjaman_id = get_object_or_404(Pinjaman, id = id)
    pinjaman_id.delete()
    return redirect('list-pinjaman')





