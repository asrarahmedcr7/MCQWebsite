# Generated by Django 4.0.6 on 2024-10-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_remove_result_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='has_answered',
            field=models.BooleanField(default=False),
        ),
    ]
