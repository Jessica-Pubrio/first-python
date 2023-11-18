
from django.db import models


# Create your models here.
class LaunchModel(models.Model):
    """
    任务启动管理表
    """
    com = models.IntegerField(verbose_name="目标平台",default=1)
    strategy = models.IntegerField(verbose_name='策略类型')
    symbol = models.CharField(max_length=100,verbose_name='交易对')
    mark = models.CharField(max_length=20,verbose_name='备注',help_text='5566',default=123)
    release = models.IntegerField(verbose_name='运行环境',default=0,help_text=9870)
    is_open = models.BooleanField(verbose_name='执行间隔',default=500,help_text='jiange')

    class Meta:
        verbose_name = '策略任务管理'
        verbose_name_plural = verbose_name
        ordering = ('-id',)

        constraints = [
            models.UniqueConstraint(fields=['com','strategy','symbol','mark'],
                                    name='launch_unique_constraint')
        ]

    def __str__(self):
        return f"com={self.com},symbol={self.symbol},strategy={self.strategy}"
