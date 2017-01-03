#_*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page
import qrcode
from io import BytesIO
# Create your views here.
@cache_page(60*5)
def index(request):
    #return HttpResponse(r'fdsfasd')
    string=u'david'
    TutorialList=["html","css","jquery","python"]
    info_dict={'site':u'baidu','content':u'python'}
    List=map(str,range(100))
    return render(request,'home.html',{'string':string,'TutorialList':TutorialList,'info_dict':info_dict,'List':List})

def formtest(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            send_mail('Subject here', 'Here is the message.%s'%str(int(a)+int(b)), 'zliu@eco-edu.cn',
                      ['12160460@qq.com'], fail_silently=False)
            return HttpResponse(str(int(a)+int(b)))
    else:
        form=AddForm()
    return  render(request,'form.html',{'form':form})

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c=int(a)+int(b)
    img = qrcode.make('http://www.juhui001.com')
    with open('test11.png', 'wb') as f:
        img.save(f)
    return HttpResponse(str(c))

def generate_qrcode(request,data):
    """
    生成二维码方法
    :param request:
    :param data: 网址
    :return: 输出二维码
    """
    img=qrcode.make(data)
    buf=BytesIO()
    img.save(buf)
    image_stream=buf.getvalue()

    response=HttpResponse(image_stream,content_type="image/png")
    response['Last-Modified']='2016-12-28 11:39:53.292890'
    response['Cache-Control']='max-age=31536000'
    return response
