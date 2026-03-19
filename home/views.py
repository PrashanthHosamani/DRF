from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Person, Color
from . serializers import PeopleSerializer, ColorSerializer


# api/i
@api_view(['GET', 'POST'])
def index(request):
    courses = {
        
        'course_name' : 'python',
        'learn' : ['flask', 'django', 'Torado', 'FastAPI'],
        'course_provider' : 'scaler'
    }
    if request.method == 'GET':
        print('you hit get method')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print("*****")
        print(data)
        print('you hit post method')
        return Response(courses)
    
    
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def people(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(objs, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        objs = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(objs, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data 
        objs = Person.objects.get(id = data['id'])
        objs.delete()
        return Response({"message" : 'Person deleted'})
    
    
    
@api_view(['GET', 'POST'])
def color(request):
    if request.method == 'GET':
        objs = Color.objects.all()
        serializer = ColorSerializer(objs, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
       data = request.data
       serializer = ColorSerializer(data = data, many =True)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors)
       