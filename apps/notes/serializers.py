from rest_framework import serializers
from apps.notes.models import Note
from collections import defaultdict
from rest_framework.exceptions import ValidationError


class NoteCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            "created_at",
            "updated_at",
            "id",
            "title",
            "description"
        ]
    

    def validate(self, attrs):
        validation_errors = defaultdict(list)
        if "title" not in attrs.keys():
            validation_errors["title"].append(
                "title field is mandatory"
            )
        if "description" not in attrs.keys():
            validation_errors["description"].append(
                "description field is mandatory"
            )

        # Raise all errors at once
        if validation_errors:
            raise ValidationError(validation_errors)

        return super().validate(attrs)


class NoteListSerializer(NoteCreateUpdateSerializer):
    class Meta(NoteCreateUpdateSerializer.Meta):
        fields = ['created_at', 'updated_at'] + NoteCreateUpdateSerializer.Meta.fields