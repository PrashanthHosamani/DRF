from rest_framework import serializers
from . models import Person, Color

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields =    '__all__'   #['name', 'age'] 
        #exclude = ['']
        
    def validate(self, data):
        
        special_characters = "!@#$%^&*()-_=+[{]}\|;:',<.>/? "
        if any( c in special_characters for c in data['name']):
            raise serializers.ValidationError("name can not contain special characters")
        
        if data['age'] < 18:
            raise serializers.ValidationError('age should be greater than 18')
        
        return data
class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = ['color_name']
    
    