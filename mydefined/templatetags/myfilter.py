from django import template
'''
过滤器主要事对上下文的内容进行操作处理

do_replace():由装饰器处理，对函数执行过滤器注册操作
参数value代表使用当前过滤器的模板上下文
参数args代表过滤器参数，函数必须返回，否则会出现异常
'''
# 创建模板对象,register名不可变，不然会报错
register = template.Library()

# 用装饰器，声明并定义过滤器，替换的方法
@register.filter(name='replace')
def do_replace(value,agrs):
    oldvalue = agrs.split(':')[0]
    newvalue = agrs.split(':')[1]
    return value.replace(oldvalue,newvalue)

# 用装饰器，再声明并定义过滤器, 返回长度得方法
@register.filter(name='get_len')
def do_get_len(l):
    count_length = len(l)
    return count_length