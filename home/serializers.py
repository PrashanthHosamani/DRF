from rest_framework import serializers
from . models import Person, Color


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    country = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields =    '__all__'   #['name', 'age'] 
        #exclude = ['']
        # depth = 1 heirarchy in depth 
        
        
    def get_country(self, obj):
        return 'india'   
        
    def validate(self, data):
        special_characters = "!@#$%^&*()-_=+[{]}\|;:',<.>/? "
        if any( c in special_characters for c in data['name']):
            raise serializers.ValidationError("name can not contain special characters")
        
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        
        return data
    


    
    