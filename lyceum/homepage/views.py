import http

from django.http import HttpResponse


def home(request):
    return HttpResponse("<body>Главная</body>")


def coffee(request):
    return HttpResponse(
        content=u"Я чайник",
        status=http.HTTPStatus.IM_A_TEAPOT,
    )
