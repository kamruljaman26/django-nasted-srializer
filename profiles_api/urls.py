#My Import
from django.conf.urls.static import static

from profiles_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

router = DefaultRouter()
router.register('tvlink',views.LiveTvViewSet)
router.register('psltvlink',views.PslLiveTvViewSet)
router.register('adservice',views.AdserviceViewSet)
router.register('matchschedule',views.MatchSchedule)
router.register('iplmatchschedule',views.IplMatchSchedule)
router.register('news',views.MatchNews)
router.register(r'devices', FCMDeviceAuthorizedViewSet)
router.register('version', views.VERSIONViewSet)


urlpatterns = [
    path('', include(router.urls)),
]