# Generated by Django 3.2.9 on 2021-12-06 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210814_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='full_desription',
            new_name='full_description',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='small_desription',
            new_name='small_description',
        ),
    ]
