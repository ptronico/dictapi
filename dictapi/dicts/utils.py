from django.db import IntegrityError

from .models import Dictionary


def get_dictionary(en_word=None, es_word=None):
    dictionary = None
    params = {'en_word': en_word} if en_word else {'es_word': es_word}
    for d in Dictionary.objects.filter(**params)[:1]:
        dictionary = d
    return dictionary


def add_dictionary(en_word, es_word):
    try:
        Dictionary.objects.create(en_word=en_word, es_word=es_word)
    except IntegrityError:
        pass


def delete_dictionary(pk):
    Dictionary.objects.filter(id=pk).delete()
