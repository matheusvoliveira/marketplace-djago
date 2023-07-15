# Generated by Django 4.2.3 on 2023-07-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('value', models.FloatField(default=0)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]