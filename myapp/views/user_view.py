from django.shortcuts import render
import requests

def user_details(request):
    id = 14
    api_response = requests.get(f'http://127.0.0.1:5001/usuarios/{id}')
    api_data = api_response.json()
    if api_response.status_code == 200:
        user_name = api_data.get('nome', 'Nome não disponível')
        return render(request, 'user_details.html', {'api_data': api_data, 'user_name': user_name})
    else:
        info_message = api_data
        return render(request, 'info.html', {'info_message': info_message})



