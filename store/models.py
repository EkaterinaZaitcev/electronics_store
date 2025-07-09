from django.db import models


class Contact(models.Model):
    """Контакт"""

    email = models.EmailField(unique=True, verbose_name="email")
    country = models.CharField(max_length=150, verbose_name="страна")
    city = models.CharField(max_length=150, verbose_name="город")
    street = models.CharField(max_length=150, verbose_name="улица")
    house_number = models.CharField(max_length=50, verbose_name="номер дома")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    """Продукт"""

    product_name = models.CharField(
        max_length=350,
        verbose_name="Название продукта",
        help_text="Укажите название продукта",
    )
    product_model = models.CharField(
        max_length=350,
        verbose_name="Модель продукта",
        help_text="Укажите модель продукта",
    )
    release_day = models.DateField(
        verbose_name="Дата выпуска", help_text="Укажите дату выпуска"
    )

    def __str__(self):
        return f"{self.product_name} ({self.product_model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name"]


class Retail(models.Model):
    """Сеть"""

    FACTORY = "factory"
    RETAIL_NETWORK = "retail_network"
    ENTREPRENEUR = "entrepreneur"
    RETAIL_TYPES = [
        (FACTORY, "Завод"),
        (RETAIL_NETWORK, "Розничная сеть"),
        (ENTREPRENEUR, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Укажите название"
    )
    contacts = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        related_name="contacts",
        verbose_name="Контакты",
        blank=True,
        null=True,
    )
    type = models.CharField(choices=RETAIL_TYPES, verbose_name="Тип сети")
    products = models.ManyToManyField(
        Product, related_name="products", verbose_name="Продукты"
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        blank=True,
        null=True,
    )
    debit = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
        verbose_name="задолженность перед поставщиком",
    )
    time_create = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)

    def __str__(self):
        return f" {self.name} - {self.type} - {self.supplier}"

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"
        ordering = [
            "name",
            "type",
        ]
