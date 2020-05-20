from django.urls import path, register_converter

from dicts import views as dict_views
from dicts.utils import LangPrefixConverter


api_prefix = 'api/v1'
register_converter(LangPrefixConverter, 'lang')


urlpatterns = [
    path(f'{api_prefix}/dictionary', dict_views.dictionary_add),
    path(f'{api_prefix}/dictionary/<int:pk>', dict_views.dictionary_delete),
    path(f'{api_prefix}/dictionary/<lang:lang>/<slug:word>', dict_views.dictionary_translate),
]
