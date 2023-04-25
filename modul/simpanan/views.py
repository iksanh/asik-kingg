from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import SimpananForm, Simpanan
from modul.crud_params import CrudParams
simpanan_param = CrudParams('simpanan')

# Create your views here.

@permission_required('view_akun')
def list_simpanan(request):
    simpanan_data = Simpanan.objects.all()
    context = simpanan_param.parameter(data=simpanan_data, simpanan=True, data_master=True)

    return render(request, 'simpanan/list_simpanan.html', context)

def create_simpanan(request):
    tempalate_file = 'simpanan/create_simpanan.html'
    if request.method == 'GET':
        context = simpanan_param.parameter(form=SimpananForm(), simpanan=True, data_master=True)
        print(context)
        return render(request, tempalate_file, context)
    elif request.method == 'POST':
        simpanan_form = SimpananForm(request.POST)
        print(request.POST)
        if simpanan_form.is_valid():
            simpanan_form.save()
            return redirect('simpanan')
        else:
            return render(request, tempalate_file, simpanan_param.parameter(form=simpanan_form, simpanan=True, data_master=True))

def edit_simpanan(request, id):
    simpanan = get_object_or_404(Simpanan, id = id)
    if request.method == 'GET':
        context = simpanan_param.parameter(form=SimpananForm(instance=simpanan), id=id, simpanan=True, data_master=True)
        return render(request, 'simpanan/create_simpanan.html', context)
    elif request.method =='POST':
        simpanan_form = SimpananForm(request.POST, instance=simpanan)
        if simpanan_form.is_valid():
            simpanan_form.save()
            return redirect('simpanan')

        else:
            return render(request, 'simpanan/create_simpanan.html', simpanan_param.parameter(form=simpanan_form, simpanan=True, data_master=True))

def delete_simpanan(request, id):
    simpanan = get_object_or_404(Simpanan, id=id)
    simpanan.delete()
    return redirect('simpanan')

def tes(request):
    return render(request, 'simpanan/login.html', context={'data': 'data'})