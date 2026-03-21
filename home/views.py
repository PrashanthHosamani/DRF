from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Person, Color
from rest_framework.views import APIView
from . serializers import PeopleSerializer, ColorSerializer, LoginSerializer
from rest_framework import viewsets



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
    # if request.method == 'GET':
    #     objs = Person.objects.all()
    #     serializer = PeopleSerializer(objs, many = True )
    #     return Response(serializer.data)
    
    if request.method == 'POST':
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
   
@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({"message" : "success"})
    return Response(serializer.errors)

class PersonAPI(APIView):  #no need to check the HTTP method to return anything, APIView authomatically campare with HTTP verb and indentifies based on name of the method 
    
    def get(self, request): #lets implement to get all the people
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        return Response("This is a post method")
    
    def put(self, request):
        return Response("This is put method")
    
    def pacth(self, request):
        return Response("This is a patch method")
    
    def delete(self, request):
        return Response("This is a delete method")
    
    

class PeopleViewSet(viewsets.ModelViewSet): #to get implement all the CRUD API's 
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    #register the router using DefaultRouter
    

