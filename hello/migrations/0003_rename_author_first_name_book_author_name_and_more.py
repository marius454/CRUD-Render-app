# Generated by Django 4.1.1 on 2022-10-09 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_first_name',
            new_name='author_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_last_name',
        ),
    ]
