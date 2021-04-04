# Generated by Django 3.1.7 on 2021-04-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meghaweb', '0003_auto_20210403_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexSectionThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SectionOneTestimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='SectionFiveIndex',
            new_name='IndexSectionFour',
        ),
        migrations.RenameModel(
            old_name='SectionOneIndex',
            new_name='IndexSectionOne',
        ),
        migrations.RenameModel(
            old_name='SectionTwoIndex',
            new_name='IndexSectionTwo',
        ),
        migrations.RenameModel(
            old_name='SectionFourIndex',
            new_name='SectionTwoTestimonials',
        ),
        migrations.DeleteModel(
            name='SectionThreeIndex',
        ),
    ]
