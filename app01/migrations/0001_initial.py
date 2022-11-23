# Generated by Django 4.1.2 on 2022-10-23 02:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('account_no', models.CharField(max_length=32, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('phone_no', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^1\\d{10}$', '手机号格式错误')], verbose_name='手机号')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_no', models.IntegerField(unique=True, verbose_name='学号')),
                ('account_no', models.CharField(max_length=32, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('grade', models.CharField(max_length=4, verbose_name='年级')),
                ('major', models.CharField(max_length=32, verbose_name='专业')),
                ('Class', models.CharField(max_length=32, verbose_name='班级')),
                ('phone_no', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^1\\d{10}$', '手机号格式错误')], verbose_name='手机号')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('account_no', models.CharField(max_length=32, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('phone_no', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^1\\d{10}$', '手机号格式错误')], verbose_name='手机号')),
            ],
        ),
    ]
