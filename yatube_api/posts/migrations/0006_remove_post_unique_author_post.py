# Generated by Django 3.2.16 on 2023-03-12 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20230312_1338'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='post',
            name='unique_author_post',
        ),
    ]
