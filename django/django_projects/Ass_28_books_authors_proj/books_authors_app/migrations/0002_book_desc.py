# Generated by Django 2.2.4 on 2022-09-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='OK'),
            preserve_default=False,
        ),
    ]
