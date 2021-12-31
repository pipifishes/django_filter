from django.contrib import admin
from django.urls import path
'''
这个py可以不设置，没有影响
'''
# 导入项目应用下视图函数中定义的函数
from temp_app.views import ind
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ind)    # 这里可以不写别名
]
