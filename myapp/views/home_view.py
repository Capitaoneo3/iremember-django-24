from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def info_page(request):
    api_data = request.GET.get('api_data', 'default_value')
    info_message = request.GET.get('info_message', 'default_message')
    return render(request, 'info.html', {'api_data': api_data, 'info_message': info_message})

