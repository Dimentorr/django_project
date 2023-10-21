import itertools

import django.core.exceptions

import catalog.models

from django.test import Client, TestCase

from parameterized import parameterized


class StaticURLTests(TestCase):
    def test_catalog_item_list_endpoint(self):
        # Делаем запрос к главной странице и проверяем её статус
        resource = Client().get("/catalog/")
        # Если возвращаемый код страницы равен 200 - тест успешно пройден
        self.assertEqual(
            resource.status_code,
            200,
            "failed check status request to /catalog/",
        )

    def test_catalog_item_detail_endpoint(self):
        # Делаем запрос к главной странице и проверяем её статус
        resource = Client().get("/catalog/4/")
        # Если возвращаемый код страницы равен 200 - тест успешно пройден
        self.assertEqual(
            resource.status_code,
            200,
            "failed check status request to /catalog/4/",
        )

    # python manage.py test
    # python ./lyceum/manage.py test
    @parameterized.expand(
        map(
            lambda x: (x[0], x[1][0], x[1][1]),
            itertools.product(
                [
                    "converter",
                    "re",
                ],
                [
                    ("1", 200),
                    ("100", 200),
                    ("-0", 404),
                    ("-100", 404),
                    ("0.5", 404),
                    ("abc", 404),
                    ("0abc", 404),
                    ("$%^", 404),
                    ("1e5", 404),
                ],
            ),
        ),
    )
    def test_catalog_item_positive_integer_endpoint(
        self,
        prefix,
        url,
        expected_status,
    ):
        full_url = f"/{prefix}/{url}/"
        response = Client().get(full_url)
        self.assertEqual(
            response.status_code,
            expected_status,
            f"failed check status request to '{full_url}'",
        )

    def test_catalog_item_positive_integer_endpoint_re_zero(self):
        response = Client().get("/re/0/")
        self.assertEqual(
            response.status_code,
            404,
            "failed check status request to '/re/0/'",
        )

    def test_catalog_item_positive_integer_endpoint_converter_zero(self):
        response = Client().get("/converter/0/")
        self.assertEqual(
            response.status_code,
            200,
            "failed check status request to '/converter/0/'",
        )


# -------------------- Data Base -----------------------


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            id=1,
            is_published=True,
            name="Тестовая категория",
            slug="test-category-slug",
            weight=100,
        )
        cls.tag = catalog.models.Tag.objects.create(
            id=1,
            is_published=True,
            name="Тестовый тэг",
            slug="test-tag-slug",
        )

    def test_unable_create_letter(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                id=1,
                name="Тестовый товар",
                category=self.category,
                text="роскошно",
            )
            self.item.full_clean()
            self.item.tags.add(ModelsTest.tag)
            self.item.save()

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count,
        )

    def test_create(self):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            id=1,
            name="Тестовый товар",
            category=self.category,
            text="1 роскошно",
        )
        self.item.tags.add(ModelsTest.tag)
        self.item.full_clean()
        self.item.save()

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1,
        )
