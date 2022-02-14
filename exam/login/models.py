from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=400,null=True)
    questionid=models.CharField(max_length=50,null=True)
    op1 = models.CharField(max_length=400,null=True)
    op2 = models.CharField(max_length=400,null=True)
    op3 = models.CharField(max_length=400,null=True)
    op4 = models.CharField(max_length=400,null=True)
    ans = models.CharField(max_length=400,null=True)
    dif =models.FloatField(null=True)
    dis=models.FloatField(null=True)
    
    def __str__(self):
        return self.question