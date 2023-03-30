from django.shortcuts import render, get_object_or_404, redirect
from .forms import AkunForm, AngsuranForm
from .models import Akun, Angsuran

# Create your views here.

def list_akun(request):
    template_list =  'transaksi/akun/list_akun.html'
    akun= Akun.objects.all()
    context = {'data': akun}
    return render(request, template_list, context )


def create_akun(request):
    template_create = 'transaksi/akun/create_akun.html'

    if request.method == 'GET':
        form = AkunForm()
        context = {'form': form}
        return render(request, template_create, context)
    elif request.method == 'POST':
        form= AkunForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('akun')
        else:
            return render(request, template_create, {'form': form})





