from django.db import models

# Create your models here.
from  django.db import models
class Question(models.Model):
    question_text=models.CharField('问题最大字数',max_length=200)
    pub_date=models.DateTimeField('date published')
class Choice(models.Model):#每个模型类似Choice，有多个变量类似question，
                            # 每个变量代表数据库中的一个字段
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
                    # 每个字段的数据类型
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)#每一个Field（类似votes）都有多个可选参数
                    #实现模型变更的三个步骤
                    #修改你的模型（在models.py文件中）。
                    #运行python manage.py makemigrations ，为这些修改创建迁移文件
                    #运行python manage.py migrate ，将这些改变更新到数据库中。