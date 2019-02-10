# Generated by Django 2.1.4 on 2019-01-03 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brief_desctiption', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(max_length=200)),
                ('money', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('brief_desctiption', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Category')),
            ],
        ),
    ]
