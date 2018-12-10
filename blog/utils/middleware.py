from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from backweb.models import Manage


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # 在访问登录和注册的时候，不需要做以下的登录校验功能
        if request.path in ['/backweb/login/','/backweb/register/']:
            return None
        # 登录验证
        else:
            user_id = request.session.get('user_id')
            if user_id:
                # 向request.user中赋值，赋值为当前的登录系统的用户对象
                user = Manage.objects.get(pk=user_id)
                request.user = user
                return None
            else:
                return HttpResponseRedirect('/backweb/login')

    def process_response(self,request,response):

        return response