import django.core.exceptions
import django.core.validators
import django.db.models


def check_two_more_words_validator(value):
    if len(str(value).split()) < 2:
        raise django.core.exceptions.ValidationError(
            "В заполняемом поле должно быть 2 и более слов",
        )


def excellent_or_luxurious_validator(value):
    if "превосходно" not in value and "роскошно" not in value:
        raise django.core.exceptions.ValidationError(
            "В тексте должно содержаться слово 'роскошно' или 'превосходно'",
        )


class AbstractModel(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        verbose_name="Опубликовано",
        default=True,
    )
    name = django.db.models.TextField(
        verbose_name="Название",
        validators=[
            django.core.validators.MaxLengthValidator(150),
        ],
    )

    class Meta:
        abstract = True


class Category(AbstractModel):
    slug = django.db.models.TextField(
        "Слаг",
        validators=[
            django.core.validators.MaxLengthValidator(200),
            django.core.validators.validate_slug,
        ],
    )
    weight = django.db.models.IntegerField(
        "Вес",
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
    )

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tag(AbstractModel):
    slug = django.db.models.TextField(
        "Слаг",
        validators=[
            django.core.validators.MaxLengthValidator(200),
            django.core.validators.validate_slug,
        ],
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Item(AbstractModel):
    name = django.db.models.TextField(
        help_text="max 150 символов",
    )
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
    )
    tags = django.db.models.ManyToManyField(Tag)
    text = django.db.models.TextField(
        "Описание",
        default="роскошно и превосходно",
        help_text="Описание должно состояить из более чем 1 слова"
        " и содержать слова 'роскошно' или 'превосходно'",
        validators=[
            check_two_more_words_validator,
            excellent_or_luxurious_validator,
        ],
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
