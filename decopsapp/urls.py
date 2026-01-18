from django.urls import path

from decopsapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('contact_Submit', views.contact_submit, name='contact_submit'),
] 