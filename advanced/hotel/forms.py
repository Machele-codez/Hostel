from django import forms
from hotel.models import Tenant

class NewTenantForm(forms.ModelForm):    
    class Meta:
        model = Tenant
        exclude = ('room',) # todo: to prevent editing value in the html (hackily)
        #// widgets = {
        #//     'room' : forms.HiddenInput(attrs={'readonly':True}),
        #// }
        