from django.contrib.auth.models import User
from rest_framework import serializers

from common.models import ParamConfig


class UserSerializer(serializers.HyperlinkedModelSerializer):
    paramconfig_set = serializers.HyperlinkedRelatedField(view_name='paramconfig-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'paramconfig_set')


class ParamConfigSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = ParamConfig
        fields = ('url', 'key', 'value', 'remark', 'creator', 'created')