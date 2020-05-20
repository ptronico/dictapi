from django.urls import path

from dicts import views as dict_views


prefix = 'api/v1'


urlpatterns = [
    path(f'{prefix}/dictionary/', dict_views.dictionary_add),
    path(f'{prefix}/dictionary/<int:pk>/', dict_views.dictionary_delete),
    path(f'{prefix}/dictionary/<slug:lang>/<slug:word>/', dict_views.dictionary_translate),
]
