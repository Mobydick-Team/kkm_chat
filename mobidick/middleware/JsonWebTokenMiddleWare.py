from http import HTTPStatus

import requests
from django.http import JsonResponse


class JsonWebTokenMiddleWare(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # 최초 설정 및 초기화

    def __call__(self, request):
        # 뷰가 호출되기 전에 실행될 코드들
        try:
            res = requests.get('http://localhost:8080/accounts/jwt/', headers={
                'Authorization': request.headers['Authorization']
            })
            request.user_id = res.json()
        except:
            return JsonResponse(
                {"error": "Authorization Error"}, status=HTTPStatus.UNAUTHORIZED
            )
        response = self.get_response(request)

        return response