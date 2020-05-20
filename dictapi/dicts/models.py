from django.db import models


class Dictionary(models.Model):
    en_word = models.CharField(max_length=40, db_index=True)
    es_word = models.CharField(max_length=40, db_index=True)

    class Meta:
        unique_together = [['en_word', 'es_word']]

    def __str__(self):
        return f'[EN] {self.en_word}: [ES] {self.es_word};'
