from django.contrib import admin

import catalog.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    # Все отображаемые поля
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    # Возможность редактировать из списка
    list_editable = (catalog.models.Item.is_published.field.name,)
    # Переход в администрирование
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # Все отображаемые поля
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    # Возможность редактировать из списка
    list_editable = (catalog.models.Category.is_published.field.name,)
    # Переход в администрирование
    list_display_links = (catalog.models.Category.name.field.name,)


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    # Все отображаемые поля
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    # Возможность редактировать из списка
    list_editable = (catalog.models.Tag.is_published.field.name,)
    # Переход в администрирование
    list_display_links = (catalog.models.Tag.name.field.name,)
