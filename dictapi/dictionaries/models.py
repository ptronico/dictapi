from django.db import models


class BaseWord(models.Model):
    word = models.CharField(max_length=40, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.word}'


class EnglishWord(BaseWord):
    pass


class SpanishWord(BaseWord):
    pass


class EnglishSpanishTranslation(models.Model):
    en_word = models.ForeignKey('dictionaries.EnglishWord', on_delete=models.CASCADE, related_name='en_words')
    es_word = models.ForeignKey('dictionaries.SpanishWord', on_delete=models.CASCADE, related_name='es_words')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['en_word', 'es_word'], name='unique_translation')
        ]

    def __str__(self):
        return f'{self.en_word} - {self.es_word}'

    def get_pair(self, lang):
        """
        Returns a tuple with word and translation pair `(word, translation)`.
        """
        return (self.en_word.word, self.es_word.word) if lang == 'en' else (self.es_word.word, self.en_word.word)

    def get_payload(self, lang):
        """
        Returns the translation payload in Python type.
        """
        return {
            'id': self.id,
            'translation': self.get_pair(lang)[1],
        }
