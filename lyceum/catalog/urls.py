from django.urls import path, re_path, register_converter

from . import converters, views


register_converter(
    converters.PositiveIntegerConverter,
    "positive",
)

urlpatterns = [
    path("catalog/", views.item_list),
    path("catalog/<int:elem>/", views.item_detail),
    # позже написать свой конвентер в файлике converters.py
    path("converter/<positive:elem>/", views.item_detail),
    # позже переписать под свою регулярное выражение
    re_path(r"^re/(?P<elem>[1-9]\d*)/$", views.item_detail),
]
