# Generated by Django 2.0.4 on 2018-04-09 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180408_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time', 'title']},
        ),
    ]
