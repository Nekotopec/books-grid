# Generated by Django 3.2 on 2021-04-22 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_storage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]