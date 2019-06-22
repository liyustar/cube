from django.urls import include, path
from rest_framework import routers
from . import apis

router = routers.DefaultRouter()
router.register(r'users', apis.UserViewSet)
router.register(r'paramconfigs', apis.ParamConfigViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]