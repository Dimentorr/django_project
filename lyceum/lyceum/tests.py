import django.test


class RussianReverseTests(django.test.TestCase):
    @django.test.override_settings(REVERSE_RUSSIAN=True)
    def test_reverse_russian_words_enabled(self):
        page_contents = {
            django.test.Client().get("/coffee/").content for _ in range(10)
        }
        self.assertIn("Я чайник".encode(), page_contents)
        self.assertIn("Я кинйач".encode(), page_contents)

    def test_reverse_russian_words_disabled(self):
        page_contents = {
            django.test.Client().get("/coffee/").content for _ in range(10)
        }
        self.assertIn("Я чайник".encode(), page_contents)
        self.assertNotIn("Я кинйач".encode(), page_contents)
