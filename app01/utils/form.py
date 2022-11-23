from django import forms
from app01.utils import encrypt , bootstrap
from app01 import models
from django.core.validators import ValidationError

class LoginForm(bootstrap.BootStrapForm):
    account_no = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        required=True
    )
    password = forms.CharField(
        label="用户名",widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"})
    )

    image_code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return encrypt.md5(pwd)

class AdminAdd(bootstrap.BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = "__all__"

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return encrypt.md5(pwd)

class StudentAdd(bootstrap.BootStrapModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return encrypt.md5(pwd)

class TeacherAdd(bootstrap.BootStrapModelForm):
    class Meta:
        model = models.Teacher
        fields = "__all__"

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return encrypt.md5(pwd)

class AdminEdit(bootstrap.BootStrapModelForm):
    class Meta:
        model = models.Admin
        exclude = ['password']
class StudentEdit(bootstrap.BootStrapModelForm):
    class Meta:
        model = models.Student
        exclude = ['stu_no','password']

class TeacherEdit(bootstrap.BootStrapModelForm):
    class Meta:
        model = models.Teacher
        exclude = ['password']

class AdminReset(bootstrap.BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}))

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]


    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = encrypt.md5(pwd)
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码不能与旧密码一致")
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        confirm = encrypt.md5(self.cleaned_data.get("confirm_password"))
        pwd = self.cleaned_data.get("password")
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm

class StudentReset(bootstrap.BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}))

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]


    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = encrypt.md5(pwd)
        exists = models.Student.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码不能与旧密码一致")
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        confirm = encrypt.md5(self.cleaned_data.get("confirm_password"))
        pwd = self.cleaned_data.get("password")
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm

class TeacherReset(bootstrap.BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "确认密码"}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}))

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]


    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = encrypt.md5(pwd)
        exists = models.Teacher.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码不能与旧密码一致")
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        confirm = encrypt.md5(self.cleaned_data.get("confirm_password"))
        pwd = self.cleaned_data.get("password")
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm