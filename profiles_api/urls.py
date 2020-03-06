#My Import
from django.conf.urls.static import static

from profiles_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('team',views.APIViewSet)



urlpatterns = [
    path('', include(router.urls)),
]