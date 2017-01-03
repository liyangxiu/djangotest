"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import os
from django.conf import settings
#from django.contrib import admindocs
from learn import  views as learn_views
#from django.contrib.admindocs import  urls as doc_urls
from django.conf.urls import include
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^$',learn_views.index),
    url(r'^form/$',learn_views.formtest,name='formtest'),
    url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
    url(r'^add/$',learn_views.add,name='add'),
    url(r'qrcode/(.+)$',learn_views.generate_qrcode,name='qrcode'),
   # url(r'^accounts/', include('users.urls')),
]
media_root = os.path.join(settings.BASE_DIR,'media')
urlpatterns += static('/media/', document_root=media_root)
