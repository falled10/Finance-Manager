# Generated by Django 2.1.4 on 2019-02-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20190210_1130'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'brief_description')},
        ),
    ]
