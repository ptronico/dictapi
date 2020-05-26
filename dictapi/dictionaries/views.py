import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .utils import clean_word, add_dictionary, get_dictionary_entries, delete_dictionary


@require_http_methods(['GET'])
def dictionary_translate(request, lang, word):
    """
    This view handles translations requests. `word` is the word
    user wants to get translated and `lang` is `word` language.
    """
    entries = get_dictionary_entries(lang=lang, word=clean_word(word))
    data = {
        'meta': {
            'lang': lang,
            'word': word,
            'entries': len(entries),
        },
        'translations': [e.get_payload(lang) for e in entries],
    }
    response = JsonResponse(data)
    response.status_code = 200 if entries else 404
    return response


@csrf_exempt
@require_http_methods(['POST'])
def dictionary_add(request):
    """
    This view handles JSON payload sent by the user and adds
    a new translation record into database. The payload should
    contains `en_word` and `es_word` fields.
    """
    try:
        payload = json.loads(request.body)
        en_word = clean_word(payload.get('en_word', ''))
        es_word = clean_word(payload.get('es_word', ''))
    except json.JSONDecodeError:
        response = JsonResponse({'message': 'Bad Request'})
        response.status_code = 400
        return response

    add_dictionary(en_word=en_word, es_word=es_word)
    response = JsonResponse({})
    response.status_code = 204
    return response


@csrf_exempt
@require_http_methods(['DELETE'])
def dictionary_delete(request, pk):
    """
    This view handle the delete task for a dictionary entry.
    """
    delete_dictionary(pk)
    response = JsonResponse({})
    response.status_code = 204
    return response
