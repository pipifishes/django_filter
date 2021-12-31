from django import template
'''
标签说对模板上下文控制输出的

render（）： 结合一个给定模板和一个给定上下文字典，并返回一个渲染后的HttpResponse对象
parse是解析器对象，当django运行时，它将所有标签和过滤器进行加载并生成到parse对象
token是被解析的对象，是模板文件使用标签时所传递的数据对象，主要包括标签名和数据内容
split_contents()：是Django的内置办法，从中获取数据，并将value传递给自定义模板节点类ReversalNode
'''
# 创建模板对象
register = template.Library()
# 类的继承；定义模板节点类
class ReversalNode(template.Node):
    def __init__(self,value):
        self.value = str(value)

    # 数据反转处理
    def render(self, context):
        return self.value[::-1]

# 用装饰器，声明并定义标签
@register.tag(name='reversal')
# parse是解析器对象，token是被解析的对象
def do_reversal(parse,token):
    try:
        tag_name,value = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')
    #调用自定义的模板节点类
    return ReversalNode(value)