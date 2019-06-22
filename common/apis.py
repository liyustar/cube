from django.contrib.auth.models import User
from rest_framework import viewsets

from common.models import ParamConfig
from common.serializers import UserSerializer, ParamConfigSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ParamConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows paramconfigs to be viewed or edited.
    """
    queryset = ParamConfig.objects.all()
    serializer_class = ParamConfigSerializer