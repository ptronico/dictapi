import string

from django.db import IntegrityError

from .models import Dictionary


def clean_word(word):
    """
    Clean `word`: validate input, remove punctuation, enforce lowercase.
    """
    return word.lower().strip().translate(str.maketrans('', '', string.punctuation))


def get_dictionary_entries(lang, word):
    """
    Get all entries with `word` in `lang`.
    """
    return list(Dictionary.objects.filter(**{f'{lang}_word__iexact': word}))


def add_dictionary(en_word, es_word):
    """
    Add a pair of `en_word` and `es_word`. The `Dictionary` model
    enforces unique pairs in the database. For this reason we are
    catching silently `IntegrityError` when tring to add a already
    existent pair.
    """
    try:
        Dictionary.objects.create(en_word=en_word, es_word=es_word)
    except IntegrityError:
        pass


def delete_dictionary(pk):
    """
    Delete a dictionary entry by its primary key.
    """
    return Dictionary.objects.filter(id=pk).delete()[0]


class LangPrefixConverter:
    """
    URL PrefixConverter for match `en|es` `lang` arguments.
    """
    regex = 'EN|En|eN|en|ES|Es|eS|es'

    def to_url(self, value):
        return f'{value}'

    def to_python(self, value):
        return value.lower()
