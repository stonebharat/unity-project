# Generated by Django 4.1.4 on 2022-12-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("upadated", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
                ("subscribed", models.BooleanField(default=True)),
            ],
        ),
    ]