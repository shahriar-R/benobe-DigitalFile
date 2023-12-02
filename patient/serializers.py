from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Patient
        # fields = ["file","doctor","test","firstname","lastname","phone","gender",]
        fields = '__all__'


        def to_representation(self, instance):
            request = self.context.get("request")
            rep = super().to_representation(instance)

            return rep
        
        def create(self, validated_data):
            return Patient.objects.create(**validated_data)
