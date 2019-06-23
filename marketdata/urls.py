from django.urls import include, path
from rest_framework import routers
from . import apis

router = routers.DefaultRouter()
router.register(r'tushare', apis.TuShareViewSet, basename='tushare')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('tushare/api/get_h_data/<str:symbol>', apis.get_h_data)
]