from django.db import models

# Create your models here.
from  django.db import models
class Question(models.Model):
    question_text=models.CharField('问题最大字数',max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
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
    def __str__(self):
        return self.choice_text#给你的模型添加__str__()方法很重要，
                                # 不仅会使你自己在使用交互式命令行时看得更加方便,
                                # 而且会在Django自动生成的管理界面中使用对象的这种表示