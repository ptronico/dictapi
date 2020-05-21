from django.urls import path, register_converter

from dictionaries import views
from dictionaries.utils import LangPrefixConverter


api_prefix = 'api/v1'
register_converter(LangPrefixConverter, 'lang')


urlpatterns = [
    path(f'{api_prefix}/dictionary', views.dictionary_add),
    path(f'{api_prefix}/dictionary/<int:pk>', views.dictionary_delete),
    path(f'{api_prefix}/dictionary/<lang:lang>/<str:word>', views.dictionary_translate),
]
