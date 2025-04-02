from django.urls import reverse
from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.views.generic.dates import timezone_today

from .models import CRM_model
from .forms import CreateTaskForm, EditTaskForm

def crm(request):
    if request.user.is_authenticated:
        type = request.GET.get('type')
        queryset = CRM_model.objects.filter(checkbox=(type == 'True'))
        error = request.GET.get('error')
        context = {'model': queryset, 'type': (type == 'True'), 'error': error}
        return render(request, 'main/index.html', context)
    else:
        return redirect_error('home:login', 'Вы не авторизированы...')

def do_task(request, id):
    if request.user.is_authenticated:
        row = CRM_model.objects.filter(id=id)
        if row.exists():
            row.update(checkbox=True, complete_date=f'{timezone_today()}')
            return redirect('main:crm')
        else:
            return redirect_error('main:crm', 'Объекта с таким id не существует...')
    else:
        return redirect_error('home:login', 'Вы не авторизированы...')

def del_task(request, id):
    if request.user.is_authenticated:
        row = None
        try:
            row = CRM_model.objects.get(id=id)
        except:
            return redirect_error('main:crm', 'Объекта с таким id не существует...')

        if row.exists():
            row.delete()
            return redirect('main:crm')

    else:
        return redirect_error('home:login', 'Вы не авторизированы...')

def create_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateTaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main:crm')
            else:
                return redirect_error('main:create_task', 'Вы ввели данные не правильно...')
        form = CreateTaskForm()
        error = request.GET.get('error')
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/create_task.html', context)
    else:
        return redirect_error('home:login', 'Вы не авторизированы...')

def change_task(request, id):
    if request.user.is_authenticated:
        task = None
        try:
            task = CRM_model.objects.get(id=id)
        except:
            return redirect_error('main:crm', 'Объекта с таким id не существует...')

        if request.method == 'POST':
            form = EditTaskForm(request.POST)
            if form.is_valid():
                task.customer_name = form.cleaned_data['customer_name']
                task.expiry_date = form.cleaned_data['expiry_date']
                task.product_description = form.cleaned_data['product_description']
                task.price = form.cleaned_data['price']
                task.contacts = form.cleaned_data['contacts']
                task.quality = form.cleaned_data['quality']
                task.type = form.cleaned_data['type']
                task.save()
                return redirect('main:crm')
            else:
                return redirect_error('main:change_task', 'Вы ввели данные не правильно...')

        if task is not None:
            inital_dict = dict({'customer_name': task.customer_name,
                           'expiry_date': task.expiry_date,
                           'product_description': task.product_description,
                           'price': task.price,
                           'contacts': task.contacts,
                           'quality': task.quality,
                           'type': task.type
            })
            form = EditTaskForm(initial=inital_dict)
            error = request.GET.get('error')
            context = {
                'form': form,
                'id':task.id,
                'error': error
            }
            return render(request, 'main/change_task.html', context)
    else:
        return redirect_error('home:login', 'Вы не авторизированы...')

def redirect_error(link, error):
    return redirect(
        f'{reverse(link)}?{urlencode(({'error': error}))}'
    )