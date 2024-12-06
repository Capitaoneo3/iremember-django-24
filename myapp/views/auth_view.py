from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from myapp.forms.user_forms import UserLoginForm,UserRegistrationForm
import requests

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = {
                'nome': form.cleaned_data['nome'],
                'senha': form.cleaned_data['senha']
            }
            api_response = requests.post('http://127.0.0.1:5001/login', json=data)
            api_data = api_response.json()
            if api_response.status_code == 200:
                success_message2 = 'Operação realizada com sucesso'
                url = reverse('info') + f'?api_data={api_data}&info_message={success_message2}'
                return HttpResponseRedirect(url)
            else:
                success_message2 = 'nao deu login'
                url = reverse('info') + f'?api_data={api_data}&info_message={success_message2}'
                return HttpResponseRedirect(url)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = {
                'nome': form.cleaned_data['nome'],
                'senha': form.cleaned_data['senha'],
                'email': form.cleaned_data['email'],
                'cpf': form.cleaned_data['cpf']
            }
            api_response = requests.post('http://127.0.0.1:5001/register', json=data)
            api_data = api_response.json()
            if api_response.status_code == 200:
                success_message = api_data
                return render(request, 'index.html', {'api_data': api_data, 'sucess_message': success_message})
            else:
                error_message = api_data
                return render(request, 'index.html', {'form': form, 'error_message': error_message})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

