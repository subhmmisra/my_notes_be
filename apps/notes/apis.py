from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import mixins
from apps.base import response
from apps.base.mixins import MultipleSerializerMixin
from apps.notes.models import Note
from apps.notes.serializers import (
    NoteCreateUpdateSerializer,
    NoteListSerializer,
)
from apps.base.pagination import paginated_response
from apps.notes.pagination import NotePageNumberPagination
from apps.base.filters import SearchWithWhitespaceFilter
from django.utils import timezone


class NoteCreateUpdateViewset(
    MultipleSerializerMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
        ):
    queryset = Note.objects.all()
    serializer_class = NoteCreateUpdateSerializer
    serializer_classes = {
        "add": serializer_class,
        "list": NoteListSerializer,
        "retrieve": NoteListSerializer,
        "update": serializer_class,
    }
    filter_backends = [SearchWithWhitespaceFilter,]
    search_fields = ["title"]

    def get_queryset(self):
        """
        Return the queryset of Note objects where the deleted_at field is null.
        """
        return Note.objects.filter(deleted_at__isnull=True)


    @action(methods=['POST'], detail=False)
    def add(self, request):
        """
        Add a new note object using the POST method and return the serialized response.
        
        Parameters:
            self: the instance of the class
            request: the request object containing the data
            
        Returns:
            The created response containing the serialized note object
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note_obj = serializer.save()
        serialized_response = self.serializer_class(note_obj).data
        return response.Created(serialized_response)
    
    def list(self, request):
        """
        This function takes a request parameter and filters the queryset based on the request. 
        It then generates a paginated response using the paginated_response function and returns an Ok response with the data.
        """
        queryset = self.filter_queryset(queryset=self.get_queryset())
        data = paginated_response(
            request,
            queryset,
            self.get_serializer_class(),
            paginator_class=NotePageNumberPagination,
        )
        return response.Ok(data.data)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve function to get object, serialize data, and return response.
        """
        instance = self.get_object()
        serializer = self.get_serializer_class()
        response_data = serializer(instance).data
        return response.Ok(response_data)
    
    def update(self, request, *args, **kwargs):
        """
        Updates an existing object with the data from the request.

        Parameters:
            request: The request object containing the data for updating the object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A response containing the updated object data.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        response_serializer = self.serializer_class(
            updated_instance, context=self.get_serializer_context()
        )
        return response.Ok(response_serializer.data)

    def delete(self, request, *args, **kwargs):
        """
        Deletes an object, sets the deletion timestamp, and returns a response with no content.
        
        Parameters:
            request: The request object
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
            
        Returns:
            NoContent response
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.deleted_at = timezone.datetime.now()
        updated_instance = serializer.save()
        return response.NoContent()
