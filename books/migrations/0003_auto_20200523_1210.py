# Generated by Django 2.0 on 2020-05-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='body',
            field=models.TextField(max_length=200),
        ),
    ]
