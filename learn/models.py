#_*_ coding:utf-8 _*_
from django.db import models
from DjangoUeditor.models import UEditorField

STATUS_CHOICES=(
    ('d','草稿'),
    ('p','已发布'),
    ('w','待发布'),
)
# Create your models here.
class Person(models.Model):
    """
    用户信息管理
    管理系统用户
    """
    name=models.CharField(u'姓名',max_length=30,help_text=u'最大长度为50')
    age=models.IntegerField(u'年龄',default=0,null=True)
    sex=models.CharField(u'性别',max_length=10,choices=(('F','男'),('M','女')),default=None)
    context=UEditorField(u'简介',width=600,height=300,toolbars='full',imagePath="images/", filePath="files/", upload_settings={"imageMaxSize":1204000},
             settings={},command=None,blank=True)#,event_handler=myEventHander()
    status=models.CharField(u'发布状态',max_length=1,choices=STATUS_CHOICES)
    editdate=models.DateTimeField(u'添加时间',auto_now_add=True)

    def __unicode__(self):
        return self.name
