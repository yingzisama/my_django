from django.contrib import admin

# Register your models here.
from .models import test_case_management

admin.site.register(test_case_management)   
admin.site.site_header = 'tc用例管理系统'
admin.site.site_title = 'tc用例管理系统'
admin.site.index_title = 'tc用例管理系统'