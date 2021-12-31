from django.contrib import admin
from django.urls import path
# 导入项目应用下视图函数中定义的函数
from temp_app.views import ind
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ind,name='inda')    # 这里一定要加上别名,在templates/index.html能用到别名
]
