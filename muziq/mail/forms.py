from django import forms

class MailForm(forms.Form):
    subject = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)