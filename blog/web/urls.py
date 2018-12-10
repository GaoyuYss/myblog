from django.conf.urls import url
from web import views

urlpatterns = [
    # 博客首页
    # 127.0.0.1:8090/web/index/
    url(r'^index/', views.index,name='index'),
    url(r'^about/',views.about,name='about'),
    url(r'^gbook/',views.gbook,name='gbook'),
    url(r'^info/(\d+)/',views.info,name='info'),
    url(r'^infopic/',views.infopic,name='infopic'),
    url('^share/',views.share,name='share')
]