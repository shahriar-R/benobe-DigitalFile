from rest_framework import serializers

from .models import Patient, Test, File





class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'


    def create(self, validated_data):
            return Test.objects.create(**validated_data)
    

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


    def create(self, validated_data):
            return File.objects.create(**validated_data)
    

class PatientSerializer(serializers.ModelSerializer):
     file = FileSerializer()
     test = TestSerializer()
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