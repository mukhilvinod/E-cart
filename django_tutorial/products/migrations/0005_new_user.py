# Generated by Django 4.1.3 on 2022-12-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('pincode', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]