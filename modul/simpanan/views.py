from django.shortcuts import render, redirect, get_object_or_404
# from modul.simpanan.models import Simpanan
from .forms import SimpananForm, Simpanan

# Create your views here.

def list_simpanan(request):
    simpanan_data = Simpanan.objects.all()
    context = {
        'simpanan' : simpanan_data
    }
    return render(request, 'simpanan/list_simpanan.html', context)

def create_simpanan(request):
    tempalate_file = 'simpanan/create_simpanan.html'
    if request.method == 'GET':
        context = {
            'simpanan_form' : SimpananForm()
        }
        return render(request, tempalate_file, context)
    elif request.method == 'POST':
        simpanan_form = SimpananForm(request.POST)
        if simpanan_form.is_valid():
            simpanan_form.save()
            return redirect('simpanan')
        else:
            return render(request, tempalate_file, {'simpanan_form' : simpanan_form})

def edit_simpanan(request, id):
    simpanan = get_object_or_404(Simpanan, id = id)
    if request.method == 'GET':
        context = {
            'simpanan_form': SimpananForm(instance=simpanan), 'id': id
        }
        return render(request, 'simpanan/create_simpanan.html', context)
    elif request.method =='POST':
        simpanan_form = SimpananForm(request.POST, instance=simpanan)
        if simpanan_form.is_valid():
            simpanan_form.save()
            return redirect('simpanan')

        else:
            return render(request, 'simpanan/create_simpanan.html', {'simpanan_form': simpanan_form})

def delete_simpanan(request, id):
    simpanan = get_object_or_404(Simpanan, id=id)
    simpanan.delete()
    return redirect('simpanan')