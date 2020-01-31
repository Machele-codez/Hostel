from django.urls import path, re_path
from hotel import views

app_name = 'hotel'

urlpatterns = [
    path('', views.RoomsListView.as_view(), name = 'rooms'),
    path('create_room/', views.RoomsCreateView.as_view(), name = 'create_room'),
    re_path(r'^room(?P<pk>\w+)/create_tenant/$', views.TenantsCreateView.as_view(), name = 'create_tenant'),
    re_path(r'^room(?P<pk>\w+)/$', views.RoomsDetailView.as_view(), name = 'room_in_detail'),
    re_path(r'^update/(?P<pk>\w+)/$', views.RoomsUpdateView.as_view(), name = 'update'),
    re_path(r'^delete/(?P<pk>\w+)/$', views.RoomsDeleteView.as_view(), name = 'delete'),
]
