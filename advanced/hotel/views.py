from .models import Tenant, Room
from django.views.generic import ListView, DetailView,TemplateView, CreateView, UpdateView, DeleteView
from .forms import NewTenantForm

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import request, HttpResponse

from .customs import create_groupings #? custom function for grouping rooms for presentation by RoomsListView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    

class RoomsListView(ListView):
    model = Room
    context_object_name = 'rooms'
    
    group = create_groupings(10) #? dictionary of all rooms in their groupings
    #! let's try using a function based view instead with the function in the model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = self.group
        #// context['objs'] = self.object_list
        return context

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
        """
        todo: getting the 'room' variable from the GET request 
        todo: (I created the variable in the url which leads to this view)
        """
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

class ManagerRegister(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    #? just like (if request.method == 'POST')
    #* def post(self, request, *args, **kwargs):
    #*     return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.success_url = reverse_lazy('login')
        form.save()
        return super().form_valid(form)
    
# Alternative function based view
# def ManagerRegister(request):

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)   

#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()

#     return render(request, 'registration/register.html', {'form':form})
