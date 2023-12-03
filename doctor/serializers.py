from rest_framework import serializers

from .models import Doctor



class DoctorSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = Doctor
        fields = '__all__'


        def to_representation(self, instance):
            request = self.context.get("request")
            rep = super().to_representation(instance)

            return rep
        
        def create(self, validated_data):
            return Doctor.objects.create(**validated_data)
