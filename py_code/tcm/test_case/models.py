from django.db import models

# Create your models here.

class test_case_management(models.Model):
    #测试用例的唯一id
    test_case_id = models.AutoField(primary_key=True)
    #测试用例的用例名
    test_case_name = models.TextField()
    #测试用例的前置操作
    test_case_preposition = models.TextField()
    #测试用例的执行步骤
    test_case_step = models.TextField()
    #测试用例的预期结果
    test_case_expected = models.TextField()
    #测试用例的实际结果
    test_case_results = models.TextField()
    #测试用例的级别P0，P1，P2
    test_case_level = models.TextField()
    #测试用例的执行人
    test_case_man = models.TextField()

    def __str__(self):
        return self.test_case_name
    