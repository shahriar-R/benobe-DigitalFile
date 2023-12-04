from rest_framework import serializers

from .models import Patient
from doctor.models import Doctor

    

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
        
    #  def create(self, validated_data):

    #     files_data = validated_data.pop('file')
    #     Patient_instance = Patient.objects.create(validated_data)
    #     for file in files_data:
    #         file.objects.create(**file)
    #     return Patient_instance 