from rest_framework import serializers

from peach.apps.university.models import Metadata


class MetadataSerializer(serializers.ModelSerializer):
    """
    Metadata Serializer
    """

    class Meta:
        """
        Metadata Serializer
        """
        model = Metadata
        fields = ["name", "type"]
