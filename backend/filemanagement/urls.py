from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileLogViewSet, FilemovementViewSet


router = DefaultRouter()
router.register(r'filelogs', FileLogViewSet)
#this says that it wants to create URLs for file logs,
# and for them to be handled by the FileLogViewSet
router.register(r'filemovements', FilemovementViewSet)
#this says that it wants to create URLs for file movements,
# and for them to be handled by the FilemovementViewSet

urlpatterns = [
    path('files/', include(router.urls)),
    #"Takes the URLs the router created and make them available at /files/."
    #So, when someone visits /files/filelogs/ or /files/filemovements/, 
    # they will reach the views that handle file logs and file movements
]
