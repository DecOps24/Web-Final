from django.urls import path

from decopsapp import views


urlpatterns = [
    path('',views.index,name='index')
] 