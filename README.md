# dictapi

This application implements a very simple English-Spanish backend dictionary acessible over a HTTP REST JSON API.

The stack is based on Python3 (and Django) and the database used is Sqlite for simplicity.

My assumptions:
 * A word may have more than one translation;
 * The amount of possible translations a word can have is only a few and does not need paginated listing;

----

## Installing and running the application


```console
$ pip install -r requirements.txt
$ python dictapi/manage.py migrate
$ python dictapi/manage.py runserver
```

The application should get running at `http://127.0.0.1:8000/`.

----

## Adding new words to dictionary

`POST /api/v1/dictionary/`

For adding new words to dictionary, send a `POST` request with a JSON payload with `en_word` and `es_word` fields as shown in the following example:

```console
$ curl -X POST http://127.0.0.1:8000/api/v1/dictionary/ \
  -data '{"en_word": "car", "es_word": "auto"}'
  {
    "status": "Created"
  }
```

----

## Getting translations

`GET /api/v1/dictionary/:language/:word/`

For getting a translation we should do a `GET` request passing a `word` and `language` as parameters in URI. For `language` we have two options `en` for English and `es` for Spanish.

```console
$ curl http://127.0.0.1:8000/api/v1/dictionary/en/car/
  {
    "meta": {
      "lang": "en",
      "word": "car",
      "entries_found": 3
    },
    "translations": [
      {
        "id": 6,
        "translation": "auto"
      },
      {
        "id": 12,
        "translation": "automobil"
      }
    ]
  }
```

----

## Deleting translations

`DELETE /api/v1/dictionary/:id/`

To delete a dictionary entry just send a `DELETE` request with `id` of the ítem that should be deleted, as the example bellow shows:

```console
$ curl -X DELETE http://127.0.0.1:8000/api/v1/dictionary/15/
```
