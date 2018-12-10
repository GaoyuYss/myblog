from django.db import models

# Create your models here.


class Manage(models.Model):
    username = models.CharField(max_length=10,unique=True,db_column='用户名',verbose_name='用户名')
    password = models.CharField(max_length=100,db_column='密码',verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True,db_column='创建时间',verbose_name='创建时间')

    class Meta:
        db_table = 'manage'


class Type(models.Model):
    name = models.CharField(max_length=20,db_column='栏目名')
    alias = models.CharField(max_length=20,db_column='别名',null=True)
    desc = models.CharField(max_length=200,db_column='描述',null=True)
    fid = models.CharField(max_length=20,db_column='父节点',null=True)

    class Mate:
        db_table = 'type'


class Article1(models.Model):
    title = models.CharField(max_length=20,db_column='标题')
    comment = models.CharField(max_length=200,unique=False,db_column='评论')
    desc = models.CharField(max_length=200,db_column='简短描述',default='')
    create_time = models.DateTimeField(auto_now_add=True,db_column='创建时间')
    content = models.TextField(db_column='内容')
    icon = models.ImageField(upload_to='article',null=True)
    visibility = models.CharField(max_length=2,db_column='是否隐藏',default='1')
    manager = models.ForeignKey(Manage,db_column='上传者',unique=False,null=True)
    type = models.ForeignKey(Type,db_column='栏目编号',null=True)

    class Meta:
        db_table = 'article'




