from django.urls import path

from decopsapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path("about_us", views.about_us, name="about_us"),
    path('contact_submit', views.contact_submit, name='contact_submit'),
] 