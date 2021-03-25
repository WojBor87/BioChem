from django.urls import path, include

from . import views

app_name = 'bio_chem'

urlpatterns = [
    path('', views.home, name='home'),

]