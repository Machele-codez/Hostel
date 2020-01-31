from django.shortcuts import render
from hostel.models import Tenant, Room
from django.views.generic import ListView, DetailView,TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hostel.forms import NewTenantForm
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
    template_name = 'hostel/rooms_details.html'


class RoomsCreateView(CreateView):
    model = Room
    fields = '__all__'


class RoomsUpdateView(UpdateView):
    model = Room
    fields = '__all__'
    

class RoomsDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('hostel:rooms')
    

class TenantsCreateView(CreateView):
    model = Tenant
    form_class = NewTenantForm #? the form_class attribute allows replacement of default CreateView form

    def form_valid(self, form):
        # todo: getting the 'room' variable from the GET request (I created the variable in the url coming to this view)
        room_num = self.request.GET.get('room')
        # todo: setting the current modelform object's room field to the value got from above
        form.instance.room = Room.objects.get(id=room_num)
        return super(TenantsCreateView, self).form_valid(form)

    #// # todo: pre-fill form data
    # ! this is inefficient as hidden inputs can be edited hackily (even with readonly attribute)
    #// """
    #// ?get_initial is a method that needs to be overrided in order to pre-fill form data
    #// ?it returns a dictionary with keys as form fields and values representing intended prefilled data
    #// """
    #// def get_initial(self):  
    #//     room = self.request.GET.get('room') #todo: getting the 'room' variable from the GET request (I created the variable in the url coming to this view) 
    #//     # print(self.request.GET)
    #//     return {
    #//         'room':room,
    #//     }
