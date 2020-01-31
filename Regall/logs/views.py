from django.shortcuts import render
from logs.forms import StudentEnrolForm

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def enrol_student(request):
    enrol_form = StudentEnrolForm()

    if request.method == 'POST':
        enrol_form = StudentEnrolForm(request.POST)

        if enrol_form.is_valid():

            enrol_form.save()
            enrol_form.set_password(enrol_form.password)
            enrol_form.save()

            print('Student, {}, just enrolled!'.format(enrol_form.cleaned_data['username']))
            return HttpResponse('<h1>Enrollment Successful</h1>')

    return render(request, 'enrol.html', {'enrol_form':enrol_form})

def student_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        student = authenticate(email = email, password = password)

        if student:
            login(request,student)
            print("Student {} successfully logged in".format(email))
            return HttpResponse('<script>alert("Logged In")</script>')
        
        else: 
            print("Failed logged in with email: {}, password: {}".format(email,password))

    return render(request, 'home.html')
    
@login_required
def logout(request):
    logout(request)
    print("logging out!")
    return render(request, 'home.html')
    
def home(request):
    return render(request, 'home.html')
