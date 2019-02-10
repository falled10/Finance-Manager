# Generated by Django 2.1.4 on 2019-01-04 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20190104_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.Category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]