# Generated by Django 2.1.2 on 2019-10-23 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='desc',
        ),
    ]
