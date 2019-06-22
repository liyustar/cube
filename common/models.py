from django.db import models

# Create your models here.

class ParamConfig(models.Model):
    '''键值配置
    Key-Value config
    '''
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    created = models.DateTimeField('config created')
