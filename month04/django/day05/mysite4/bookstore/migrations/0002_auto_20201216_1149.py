# Generated by Django 2.2.12 on 2020-12-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(max_length=3, verbose_name='年龄')),
            ],
            options={
                'verbose_name_plural': '作者',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': '图书'},
        ),
    ]
