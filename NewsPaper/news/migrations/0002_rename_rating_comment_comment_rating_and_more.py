# Generated by Django 4.1.6 on 2023-02-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='rating_comment',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postrating',
            new_name='rating',
        ),
    ]