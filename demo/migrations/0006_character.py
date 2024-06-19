# Generated by Django 5.0.6 on 2024-06-19 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0005_booknumber_book_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=30)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="demo.book"
                    ),
                ),
            ],
        ),
    ]
