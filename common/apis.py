from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from common.models import ParamConfig
from common.permissions import IsAdminUserOrReadOnly
from common.serializers import UserSerializer, ParamConfigSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    # permission_classes = (permissions.IsAdminUser,)


class ParamConfigViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows paramconfigs to be viewed or edited.
    """
    queryset = ParamConfig.objects.all()
    serializer_class = ParamConfigSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(creator=self.request.user)
        else:
            serializer.save()
