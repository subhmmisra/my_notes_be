from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.notes.apis import NoteCreateUpdateViewset

default_router = DefaultRouter(trailing_slash=False)


default_router.register("note", NoteCreateUpdateViewset, basename="notes-v1")
#default_router.register("users", UserViewset, basename="users")

urlpatterns = default_router.urls