from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from apps.debitos.models import Debitos


class DebitosDetail(DetailView):
    model = Debitos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        

class DebitoList(LoginRequiredMixin, ListView):
    login_url = '/login'
    Model = Debitos

    def get_queryset(self):
        return Debitos.objects.all()


class DebitoCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'

    model = Debitos
    fields = ['valor', 'produto', 'observacao', 'categoria', 'tipo', 'credor', 'parcelas', 'status', 'vencimento',
              'hrs_trab_pagar']
    success_url = '/debitos/list'


class DebitosUpdate(UpdateView):
    model = Debitos
    fields = ['valor', 'produto', 'observacao', 'categoria', 'tipo', 'credor', 'parcelas', 
                'status', 'vencimento', 'hrs_trab_pagar']
    success_url ='/debitos/list'


class DebitosDelete(DeleteView):
    model = Debitos
    
    success_url='/debitos/list'