# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from myapp.forms.post_forms import PostForm
import requests

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Preparar os dados para enviar para a API externa
            data = {
                'titulo': form.cleaned_data['titulo'],
                'conteudo': form.cleaned_data['conteudo'],
                'autor_id': 3  # Substitua com o ID real do autor se necessário
            }
           
            try:
                # Enviar dados para a API externa
                api_response = requests.post('http://127.0.0.1:5001/posts', json=data)
                api_response.raise_for_status()  # Levanta um erro para respostas de erro HTTP
               
                # Tentar obter dados da resposta JSON
                api_data = api_response.json()
               
                if api_response.status_code == 201:
                    success_message2 = 'Post criado com sucesso'
                else:
                    success_message2 = 'Erro ao criar o post'
           
            except requests.RequestException as e:
                # Em caso de erro na requisição ou na resposta
                api_data = {}
                success_message2 = 'Erro ao criar o post: ' + str(e)
           
            # Redirecionar com mensagem de sucesso ou erro
            url = reverse('info') + f'?api_data={api_data}&info_message={success_message2}'
            return HttpResponseRedirect(url)
        else:
            # Se o formulário não for válido, retornar erros no formato JSON
            return JsonResponse({"message": "Erro ao criar o post", "errors": form.errors}, status=400)
    else:
        form = PostForm()
   
    # Renderizar o formulário para o GET
    return render(request, 'create_post.html', {'form': form})

