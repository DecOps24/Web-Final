from django.urls import path

from decopsapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('contact_Submit', views.contact_submit, name='contact_submit'),
    path("home_page",views.home_page,name="home_page"),
    path('services',views.services,name="services"),
    path("about_us",views.about_us,name="about_us"),
] 