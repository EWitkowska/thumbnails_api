# Generated by Django 4.2.7 on 2024-02-11 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("thumbnails", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="expiringlink",
            name="image",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="thumbnails.image"
            ),
        ),
        migrations.AddField(
            model_name="expiringlink",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
