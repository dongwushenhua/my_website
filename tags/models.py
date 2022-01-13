from django.db import models
from datetime import datetime


class tag(models.Model):
    tagName = models.CharField(max_length=64, null=False, verbose_name='标签名', error_messages={'yonghuming': '长度必须为'})
    createTime = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    tagCreater = models.ForeignKey("users.userProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.tagName

    class Meta:
        db_table = 'tag'
