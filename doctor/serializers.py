from rest_framework import serializers

from .models import Doctor, Secretary



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
        
class SecretarySerializer(serializers.ModelSerializer):
     
     class Meta:
        model = Secretary
        fields = '__all__'


        def to_representation(self, instance):
            request = self.context.get("request")
            rep = super().to_representation(instance)

            return rep
        
        def create(self, validated_data):
            return Secretary.objects.create(**validated_data)

