from django.urls import path

from decopsapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path("home_page",views.home_page,name="home_page"),
    path('services',views.services,name="services")
] 