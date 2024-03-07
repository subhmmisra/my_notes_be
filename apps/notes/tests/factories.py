from django.apps import apps
from django_dynamic_fixture import G


def create_note(**kwargs):
    Note = apps.get_model("notes", "Note")
    title = kwargs.pop("title", None) or "title_1"
    description = kwargs.pop("description", None) or "descripition_1"
    return G(Note, title=title, description=description, **kwargs)