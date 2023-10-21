import http

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        # Делаем запрос к главной странице и проверяем её статус
        resource = Client().get("")
        # Если возвращаемый код страницы равен 200 - тест успешно пройден
        self.assertEqual(
            resource.status_code,
            200,
            "Что-то пошло не так с главной страницей",
        )

    def test_coffe_endpoint_status(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)

    def test_coffe_endpoint_test(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.content, "Я чайник".encode())
