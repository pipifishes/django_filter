from django.shortcuts import render
'''
利用 Python 的内建函数 locals() 。它返回的字典对所有局部变量的名称与值进行映射
'''

# Create your views here.
def ind(request):
    value = 'hellohi python'  # value用于myfilter;index.html
    return render(request,'index.html',locals())
    # 原本再myfilter中新增了一个过滤器get_len，是需要在加上一个render关联返回content，但是locals()可以映射所用
    # return render(request,'index.html',context=value)











