from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.products, name='prod'),
    path('about', views.about, name='about'),
    path('ceo', views.ceo, name='ceo'),
    path('cvo', views.cvo, name='cvo'),
    path('doc', views.doc, name='doc'),
    path('employees', views.employees, name='employees'),
    path('contact', views.contact, name='contact')
]
