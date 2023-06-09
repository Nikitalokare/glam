# Generated by Django 4.1.6 on 2023-03-03 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_alter_product_category_product_cate_name'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qunt', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userinfo')),
            ],
            options={
                'db_table': 'Mycart',
            },
        ),
    ]
