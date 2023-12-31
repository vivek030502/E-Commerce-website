# Generated by Django 4.2.7 on 2023-11-26 06:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("E_Mart", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Code",
            new_name="Color",
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "unique_id",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                ("image", models.ImageField(upload_to="Product_images/img")),
                ("name", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                (
                    "condition",
                    models.CharField(
                        choices=[("New", "New"), ("Old", "Old")], max_length=100
                    ),
                ),
                ("information", models.TextField()),
                ("description", models.TextField()),
                (
                    "stock",
                    models.CharField(
                        choices=[
                            ("IN STOCK", "IN STOCK"),
                            ("OUT OF STOCK", "OUT OF STOCK"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Publish", "Publish"), ("Draft", "Draft")],
                        max_length=200,
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "Categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="E_Mart.categories",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="E_Mart.brand"
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="E_Mart.color"
                    ),
                ),
                (
                    "filter_price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="E_Mart.filter_price",
                    ),
                ),
            ],
        ),
    ]
