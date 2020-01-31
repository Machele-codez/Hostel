from django.urls import path
from logs import views

app_name = 'logs'

urlpatterns = [
    path('enrol_student', views.enrol_student, name = 'enrol_student'),
    path('student_login', views.student_login, name = 'student_login'),
    path('logout', views.logout, name = 'logout'),

]
