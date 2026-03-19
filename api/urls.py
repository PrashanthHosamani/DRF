from home.views import index, people, color
from django.urls import path

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('index/', index),
    path('people/', people),
    path('color/', color),
]
