from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Student(models.Model):
    stu_no = models.IntegerField(verbose_name="学号", unique=True)
    # stu_no = models.CharField(max_length=15, verbose_name="学号", unique=True, null=True, blank=True)
    name = models.CharField(verbose_name="姓名", max_length=32)
    account_no = models.CharField(verbose_name="账号", unique=True, max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    grade = models.CharField(verbose_name="年级", max_length=4)
    major = models.CharField(verbose_name="专业", max_length=32)
    Class = models.CharField(verbose_name="班级", max_length=32)
    phone_no = models.CharField(verbose_name="手机号", max_length=11, unique=True,
                              validators=[RegexValidator(r'^1\d{10}$', "手机号格式错误")])


class Teacher(models.Model):

    name = models.CharField(verbose_name="姓名", max_length=32)
    account_no = models.CharField(verbose_name="账号", unique=True, max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    phone_no = models.CharField(verbose_name="手机号", max_length=11, unique=True,
                              validators=[RegexValidator(r'^1\d{10}$', "手机号格式错误")])


class Admin(models.Model):

    name = models.CharField(verbose_name="姓名", max_length=32)
    account_no = models.CharField(verbose_name="账号", unique=True, max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    phone_no = models.CharField(verbose_name="手机号", max_length=11, unique=True,
                              validators=[RegexValidator(r'^1\d{10}$', "手机号格式错误")])