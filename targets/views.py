from django.shortcuts import render
from .models import Alvo
from .forms import AlvoForm

def mapa_view(request):
    form = AlvoForm()
    alvos = Alvo.objects.all()
    return render(request, 'targets/mapa.html', {'form': form, 'alvos': alvos})
