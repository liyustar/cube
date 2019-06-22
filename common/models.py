from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ParamConfig(models.Model):
    '''键值配置
    Key-Value config
    '''
    key = models.CharField(unique=True, max_length=100)
    value = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    creator = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_constraint=False,
        related_name="paramconfig_set",
        related_query_name="paramconfig",
    )
    created = models.DateTimeField('config created')
