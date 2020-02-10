from django.shortcuts import render
from hotel.models import Tenant, Room
from django.views.generic import ListView, DetailView,TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hotel.forms import NewTenantForm
from django.http import request

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class RoomsListView(ListView):
    model = Room
    context_object_name = 'rooms'


class RoomsDetailView(DetailView):
    model = Room
    context_object_name = 'room_in_detail'
    template_name = 'hotel/rooms_details.html'


class RoomsCreateView(CreateView):
    model = Room
    fields = '__all__'


class RoomsUpdateView(UpdateView):
    model = Room
    fields = '__all__'
    

class RoomsDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('hotel:rooms')


class TenantsDetailView(DetailView):
    model = Tenant
    context_object_name = 'tenant_in_detail'


class TenantsCreateView(CreateView):
    model = Tenant
    # ? the form_class attribute allows replacement of default CreateView form
    form_class = NewTenantForm

    def form_valid(self, form):
        # todo: getting the 'room' variable from the GET request (I created the variable in the url coming to this view)
        room_num = self.request.GET.get('room')
        # todo: setting the current modelform's room field to the value gotten from above
        form.instance.room = Room.objects.get(number=room_num)
        return super(TenantsCreateView, self).form_valid(form)


class TenantsDeleteView(DeleteView):
    model = Tenant

    # todo: override get_success_url to pass in GET variable as argument for redirection url after object deletion
    def get_success_url(self):
        room_num = self.request.GET['room']
        return reverse_lazy('hotel:room_in_detail', kwargs = {'pk':room_num})

