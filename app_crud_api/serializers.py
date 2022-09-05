from rest_framework import serializers
from .models  import Student
class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self , instance , validated_data):
        instance.name = validated_data.get('name' , instance.name) 
        instance.roll = validated_data.get('roll' , instance.name) 
        instance.city = validated_data.get('city' , instance.name) 