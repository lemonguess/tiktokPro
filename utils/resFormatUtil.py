from django.http import JsonResponse


class ResFormat:
    SUCCESS = 0, '成功'  # status
    PARAM_ERROR = 4001, '参数错误'
    UNKNOWN_ERROR = 4100, '未知错误'
    ACCESS_RESTRICTION = 4002, '访问限制'
    ACCOUNT_REGISTRATION = 4003, '账户已注册'
    CODE_EXPIRED = 4004, '验证码已过期'

    def __init__(self, status='SUCCESS', data=''):
        """
        初始化
        """
        if hasattr(self, status):
            status = getattr(self, status)  # 获取指定对象的指定属性
        else:
            status = self.UNKNOWN_ERROR
        self.code, self.msg = status
        self.data = data

    def res(self):
        dic = {'code': self.code}

        if self.msg:
            dic['msg'] = self.msg
        if self.data:
            dic['data'] = self.data
        return dic

    def json_response(self):
        """
        返回转回以后的json响应对象
        :return:  JsonResponse
        """
        return JsonResponse(self.res(), json_dumps_params={'ensure_ascii': False})
