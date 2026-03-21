from home.views import index, people, color, login, PersonAPI, PeopleViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', PeopleViewSet, basename= 'user')
urlpatterns = router.urls

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('index/', index),
    path('people/', people),
    path('color/', color),
    path('login/', login),
    path('persons/', PersonAPI.as_view()), #dealing with the classs
    path('', include(router.urls))
    
]
