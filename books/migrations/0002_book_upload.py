# Generated by Django 2.0 on 2020-05-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
