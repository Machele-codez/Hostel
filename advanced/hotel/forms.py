from django import forms
from hotel.models import Tenant

class NewTenantForm(forms.ModelForm):    
    class Meta:
        model = Tenant
        exclude = ('room',) # todo: to prevent editing value in the html (hackily)
        #// widgets = {
        #//     'room' : forms.HiddenInput(attrs={'readonly':True}),
        #// }
    
    # todo: to clean the student_ID field
    def clean_student_ID(self):
        student_id = self.cleaned_data.get('student_ID')
        print(student_id)
        for i in student_id:
            if i not in '0123456789':
                raise(forms.ValidationError('student_ID must contain only numbers'))
        if len(student_id) != 10:
            raise(forms.ValidationError('student_ID must consist of ten characters'))
        return student_id
