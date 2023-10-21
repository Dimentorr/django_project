from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        # Делаем запрос к главной странице и проверяем её статус
        resource = Client().get("/about/")
        # Если возвращаемый код страницы равен 200 - тест успешно пройден
        self.assertEqual(
            resource.status_code,
            200,
            "Что-то пошло не так со страницей 'О нас'",
        )
