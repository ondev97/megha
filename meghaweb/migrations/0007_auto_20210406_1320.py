# Generated by Django 3.1.7 on 2021-04-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meghaweb', '0006_auto_20210406_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexsectionfour',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='indexsectionone',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='indexsectionthree',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ordersection',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='orderstep',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='testimonialssectionone',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='testimonialssectiontwo',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
