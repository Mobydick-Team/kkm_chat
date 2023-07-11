from http import HTTPStatus

from django.http import JsonResponse

from mobidick.settings import JWT_SECRET_KEY
from chat.utils.getUserId import getUserId


class JsonWebTokenMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # 최초 설정 및 초기화

    def __call__(self, request):
        # 뷰가 호출되기 전에 실행될 코드들
        try:
            if request.path != '/swagger/':
                jwt = request.headers['Authorization'].split(' ')[1];
                request.user_id = getUserId(jwt)
        except:
            return JsonResponse(
                {"error": "Authorization Error"}, status=HTTPStatus.UNAUTHORIZED
            )
        response = self.get_response(request)

        return response