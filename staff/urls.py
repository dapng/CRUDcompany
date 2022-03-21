from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_home, name='staff'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.StaffDetailView.as_view(), name='staff-detail'),
    path('<int:pk>/update', views.StaffUpdateView.as_view(), name='staff-update'),
    path('<int:pk>/delete', views.StaffDeleteView.as_view(), name='staff-delete')
]
