# Generated by Django 3.2.6 on 2021-08-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210814_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='desription',
            new_name='small_desription',
        ),
        migrations.AddField(
            model_name='blogs',
            name='full_desription',
            field=models.CharField(default='', max_length=1000),
        ),
    ]