# Generated by Django 4.1.7 on 2023-05-03 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_health', '0006_disease_user_descpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
                ('productprice', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='disease_user',
            name='productname',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='disease_user',
            name='precaution',
            field=models.CharField(max_length=500),
        ),
    ]
