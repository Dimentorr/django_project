from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, elem):
    return HttpResponse("<body>Подробно элемент</body>")
