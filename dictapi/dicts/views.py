import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .utils import add_dictionary, get_dictionary, delete_dictionary


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def dictionary(request):
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        response = JsonResponse({'message': 'Bad Request'})
        response.status_code = 400
        return response

    if request.method == 'GET':
        # Getting a directionary entry
        d = get_dictionary(en_word=payload.get('en_word', ''), es_word=payload.get('es_word', ''))
        if d:
            data = {
                'id': d.id,
                'en_word': d.en_word,
                'es_word': d.es_word,
            }
            return JsonResponse(data)

        response = JsonResponse({'message': 'Not Found'})
        response.status_code = 404
        return response

    if request.method == 'POST':
        # Creating a new dictionary entry
        add_dictionary(en_word=payload.get('en_word', ''), es_word=payload.get('es_word', ''))
        request = JsonResponse({'status': 'success'})
        request.status_code = 201
        return request


@csrf_exempt
@require_http_methods(['DELETE'])
def dictionary_delete(request, pk):
    delete_dictionary(pk)
    return JsonResponse({'status': 'success'})
