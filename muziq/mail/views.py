from django.shortcuts import render
from .forms import MailForm
from django.http import HttpResponse
from django.core.mail import send_mail
from muziq.settings import EMAIL_HOST_USER

# Create your views here.
def home(request):
    form = MailForm()
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            subject = str(form.cleaned_data['subject'])
            message = str(form.cleaned_data['message'])
            recipients = ['']
            send_mail(subject=subject, message=message,from_email=EMAIL_HOST_USER,recipient_list=recipients,fail_silently=False)
            print('MAIL SENT!!!!!!!!!!!!!!!')
            return HttpResponse('<h1>Thanks</h1>')
    return render(request, 'mails.html',{'form':form})