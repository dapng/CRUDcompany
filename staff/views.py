from dataclasses import field
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from .models import Employ
from .forms import EmployForm
from django.views.generic import DeleteView, DetailView, UpdateView


def staff_home(request):
    emp = Employ.objects.all()
    return render(request, 'staff/employees.html', {'emp': emp})


class StaffDetailView(DetailView):
    model = Employ
    template_name = 'staff/detail_view.html'
    context_object_name = 'staff'


class StaffUpdateView(UpdateView):
    model = Employ
    template_name = 'staff/update.html'

    form_class = EmployForm


class StaffDeleteView(DeleteView):
    model = Employ
    success_url = '/staff/'
    template_name = 'staff/delete.html'


def create(request):
    if request.method == 'POST':
        form = EmployForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('.')
        else:
            error = 'Форма не верна!'
            
    form = EmployForm()

    data = {
        'form': form
    }
    return render(request, 'staff/create.html', data)

