from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from backweb.models import Manage, Article1
from django.core.paginator import Paginator
from backweb.Artform import AddArtForm ,TypeForm
from backweb.models import Type


# 注册
def register(request):
    # 通过register路由进入函数一开始是GET请求方式
    if request.method == 'GET':
        # GET 访问http://127.0.0.1:8000/register/
        return render(request,'backweb/register.html')

    # 在register.html中的请求方式是POST方式
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        password2 = request.POST.get('userpwd2')

        # 判断用户名是否已经被注册过
        user = Manage.objects.filter(username=username).first()
        if user:
            err = '该账号已经被注册'
            return render(request,'backweb/register.html',{'err':err})
        # 判断输入的用户名是否为空
        if username == '':
            err = '用户名不能为空'
            return render(request,'backweb/register.html',{'err':err})

        # 判断密码和确认密码是否相同
        if password and password2:
            if password != password2:
                err_pwd = '密码和确认密码不一致，请修改密码'
                data = {'err':err_pwd}
                return render(request,'backweb/register.html',data)
            # 实现注册
            else:
                Manage.objects.create(username=username, password=password)
                # 跳转到登录页面
                return HttpResponseRedirect(reverse('backweb:login'))

        # 判断密码是否都有
        else :
            err_pwd = '密码不能为空'
            data = {'err':err_pwd}
            return render(request, 'backweb/register.html', data)


# 登录
def login(request):
    if request.method == 'GET':
        return render(request,'backweb/login.html')
    if request.method == 'POST':
        # 1.获取登录提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('userpwd')

        # 2.查询数据库中用户名和密码对应的用户对象
        user = Manage.objects.filter(username=username,password=password).first()
        # 比对失败
        if not user:
            err = '用户名或者密码错误'
            return render(request,'backweb/login.html',{'err':err})
        # 比对成功
        else:
            request.session['user_id'] = user.id
            res = HttpResponseRedirect(reverse('backweb:index'))
            return res


# 退出
def logout(request):
    # 删除django_session表中的数据
    # request.session.delete(request.session.session_key)
    # 删除session_data中登录成功后设置的键值对
    del request.session['user_id']
    return HttpResponseRedirect('/backweb/login/')


# 首页
def index(request):
    if request.method == 'GET':
        print('shide')
        return render(request,'backweb/index.html')


# 文章列表
def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        article = Article1.objects.filter(visibility='1')
        paginator = Paginator(article,2)
        page = paginator.page(page)
        return render(request,'backweb/article.html',{ 'page':page })


# 增加文章
def add_article(request):
    if request.method == 'GET':
        types = Type.objects.all()
        return render(request,'backweb/add-article.html',{'types':types})
    if request.method == 'POST':
        form = AddArtForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            describe = form.cleaned_data['describe']
            pic = form.cleaned_data['pic']
            typ = form.cleaned_data['category']
            type = Type.objects.filter(id=typ).first()
            visibility = form.cleaned_data['visibility']
            Article1.objects.create(title=title,content=content,desc=describe,
                                   type=type,icon=pic,visibility=visibility)
            return HttpResponseRedirect(reverse('backweb:article'))
        else :
            return  HttpResponseRedirect(reverse('backweb:add_article'))


# 删除文章
def delete(request,id):
    if request.method == 'GET':
        Article1.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))


# 更新文章
def update_article(request,id):
    if request.method == 'GET':
        article = Article1.objects.filter(pk=id).first()
        types = Type.objects.all()
        return render(request,'backweb/add-article.html',{'article':article,'types':types})

    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            # 验证成功
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            desc = form.cleaned_data['describe']

            typ = form.cleaned_data['category']
            type = Type.objects.filter(id=typ).first()
            icon = form.cleaned_data['pic']
            visibility = form.cleaned_data['visibility']
            article = Article1.objects.filter(pk=id).first()
            article.title = title
            article.desc = desc
            article.content = content
            article.type = type
            article.visibility = visibility
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            # 验证失败
            article = Article1.objects.filter(pk=id).first()
            return  HttpResponseRedirect(reverse('backweb:update_article'))


def category(request):
    if request.method == 'GET':
        types = Type.objects.all()
        return render(request,'backweb/category.html',{'types':types})
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            fid = form.cleaned_data['fid']
            desc = form.cleaned_data['describe']
            Type.objects.create(name=name,alias=alias,fid=fid,desc=desc)
            return HttpResponseRedirect(reverse('backweb:category'))
        else:
            return render(request,'backweb/category.html')


def update_category(request,id):
    if request.method == 'GET':
        typ = Type.objects.filter(pk=id).first()
        return render(request,'backweb/update-category.html',{'typ':typ})
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            alias = form.cleaned_data['alias']
            fid = form.cleaned_data['fid']
            desc = form.cleaned_data['describe']
            typ = Type.objects.filter(pk=id).first()
            typ.name = name
            typ.alias =alias
            typ.fid = fid
            typ.save()
            return HttpResponseRedirect(reverse('backweb:category'))
        else:
            return HttpResponseRedirect(reverse('backweb:update_category'))


def delete_category(request,id):
    if request.method == 'GET':
        Type.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:category'))


def link(request):
    if request.method == 'GET':
        return render(request,'backweb/flink.html')
    if request.method == 'POST':
        return render(request,'backweb/flink.html')


def manage_user(request):
    if request.method == 'GET':
        return render(request,'backweb/manage-user.html')


def loginlog(request):
    if request.method == 'GET':
        return render(request, 'backweb/loginlog.html')






def add_flink(request):
    pass


def add_notice(request):
    pass


def notice(request):
    if request.method == 'GET':
        return render(request,'backweb/notice.html')


def comment(request):
    pass














def readset(request):
    pass


def setting(request):
    pass


def update_flink(request):
    pass