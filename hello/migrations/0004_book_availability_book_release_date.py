# Generated by Django 4.1.1 on 2022-10-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_rename_author_first_name_book_author_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='availability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='release_date',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
