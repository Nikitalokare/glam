# Generated by Django 4.1.6 on 2023-03-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_mycart_shade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='shade',
            field=models.CharField(default='No shade', max_length=20),
        ),
    ]