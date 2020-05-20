from django.urls import path

from dicts import views as dict_views


urlpatterns = [
    path('dictionary/', dict_views.dictionary),
    path('dictionary/<int:pk>/', dict_views.dictionary_delete),
]
