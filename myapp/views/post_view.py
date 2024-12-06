import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import render

def listar_posts(request):
    try:
        # URL da API Flask
        url = 'http://127.0.0.1:5001/posts'  # ajuste o endereço e a porta conforme necessário

        # Enviar requisição GET para a API Flask
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP de erro

        # Verificar se a resposta contém dados
        posts = response.json()

        # Configurar a paginação
        paginator = Paginator(posts, 5)  # Exibir 5 posts por página
        page_number = request.GET.get('page')  # Obter o número da página da URL
        page_obj = paginator.get_page(page_number)  # Retorna os posts da página solicitada

        # Renderizar o template com os posts e a paginação
        return render(request, 'listar_posts.html', {'page_obj': page_obj})

    except requests.RequestException as e:
        # Em caso de erro na requisição
        return HttpResponse(f"Erro ao buscar os posts: {e}", status=500)
