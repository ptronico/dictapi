from django.db import models


class Dictionary(models.Model):
    en_word = models.CharField(max_length=40, db_index=True)
    es_word = models.CharField(max_length=40, db_index=True)

    class Meta:
        ordering = ['en_word', 'es_word']
        unique_together = [['en_word', 'es_word']]

    def __str__(self):
        return f'[EN] {self.en_word}: [ES] {self.es_word};'

    def get_pair(self, lang):
        """
        Returns a tuple with word and translation pair `(word, translation)`.
        """
        return (self.en_word, self.es_word) if lang == 'en' else (self.es_word, self.en_word)

    def get_payload(self, lang):
        """
        Returns the translation payload in Python type.
        """
        return {
            'id': self.id,
            'translation': self.get_pair(lang)[1],
        }
