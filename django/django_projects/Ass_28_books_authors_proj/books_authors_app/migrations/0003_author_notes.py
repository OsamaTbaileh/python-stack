# Generated by Django 2.2.4 on 2022-09-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='--'),
            preserve_default=False,
        ),
    ]
