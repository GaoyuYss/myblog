from django.conf.urls import url

from backweb import views


app_name = 'backweb'
urlpatterns = [
    # 127.0.0.1:8090/backweb/login/
    # 登录
    url(r'^login/', views.login,name='login'),
    # 首页
    url(r'^index/',views.index,name='index'),
    # 注册
    url(r'^register/',views.register,name='register'),
    # 文章页
    # 127..0.0.1/backweb/article/?page=2
    # 127..0.0.1/backweb/article/2/
    # 文章展示
    url(r'^article/',views.article,name='article'),
    # 添加文章
    url(r'^add_article',views.add_article,name='add_article'),
    # 删除文章
    url(r'^delete/(\d+)/',views.delete,name='delete'),
    # 修改文章
    url(r'^update_article/(\d+)/',views.update_article,name='update_article'),
    # 栏目列表与增加栏目
    url(r'^category', views.category, name='category'),
    # 更新栏目
    url(r'^update_category/(\d+)/', views.update_category, name='update_category'),
    # 删除栏目
    url(r'^delete_category/(\d+)/',views.delete_category,name='delete_category'),
    # 友情链接
    url(r'^link/',views.link,name='link'),
    # 退出登录
    url(r'^logout/',views.logout,name='logout'),


    url(r'^add_flink',views.add_flink,name='add_flink'),
    url(r'^add_notice',views.add_notice,name='add_notice'),
    url(r'^comment',views.comment,name='comment'),
    url(r'^loginlog',views.loginlog,name='loginlog'),
    url(r'^manage_user',views.manage_user,name='manage_user'),
    url(r'^notice',views.notice,name='notice'),
    url(r'^readset',views.readset,name='readset'),
    url(r'^setting',views.setting,name='setting'),
    url(r'^update_flink',views.update_flink,name='update_flink'),




]