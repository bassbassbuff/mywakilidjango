from rest_framework import serializers

from .models import Matter, File ,Client


class MatterSerializer(serializers.ModelSerializer):
    # client = serializers.StringRelatedField()
    
    class Meta:
        model = Matter
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = (
            "id",
            "name",
            "client",
            "description",
            "client_name",
            "client_address2",
            "client_zipcode",
            "client_place",
            "client_county",
            "client_contact_person",
            "client_contact_reference"
        )
    

    def create(self, validated_data):        
        matter = Matter.objects.create(**validated_data)    
        return matter

