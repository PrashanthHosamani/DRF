from rest_framework.decorators import api_view
from rest_framework.response import Response



# api/i
@api_view(['GET'])
def index(request):
    courses = {
        
        'course_name' : 'python',
        'learn' : ['flask', 'django', 'Torado', 'FastAPI'],
        'course_provider' : 'scaler'
    }
    
    return Response(courses)
