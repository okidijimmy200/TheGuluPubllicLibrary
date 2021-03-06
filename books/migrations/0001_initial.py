# Generated by Django 2.0 on 2020-05-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('S', 'Science Fiction'), ('D', 'Drama'), ('H', 'History'), ('C', 'Crime')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='timestamp')),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
