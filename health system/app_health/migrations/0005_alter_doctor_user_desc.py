# Generated by Django 4.1.7 on 2023-05-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_health', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_user',
            name='desc',
            field=models.CharField(max_length=1500),
        ),
    ]
