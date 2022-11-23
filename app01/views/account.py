# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from app01.utils.form import LoginForm
from app01.utils.code import check_code
from io import BytesIO

def login(request):

    return render(request, 'choose_character.html')

def image_code(request):
    #生成文件验证码
    img, code_string = check_code()

    request.session['image_code'] = code_string
    request.session.set_expiry(60)  # 主动修改session的过期时间为60s

    # # 把图片写入文件
    # with open('code.png', 'wb') as f:
    #     img.save(f, format='png')

    # 把图片的内容写到内存stream
    stream = BytesIO()
    img.save(stream, format='png')
    return HttpResponse(stream.getvalue())

def login_admin(request):
    title = "管理员登录"
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"title": title, "form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop("image_code")
        image_code = request.session.get("image_code", "")
        if image_code != user_input_code.upper():
            form.add_error("image_code", "验证码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()

        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        request.session["info"] = {"id": admin_object.id, "username": admin_object.account_no, "actor": "admin"}
        request.session.set_expiry(60 * 60 * 27)
        return redirect('/list/admin/')

    return render(request, 'login.html', {"title": title, "form": form})

def login_student(request):
    title = "学生登录"
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"title" : title, "form":form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop("image_code")
        image_code = request.session.get("image_code", "")
        if image_code != user_input_code.upper():
            form.add_error("image_code", "验证码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        sutdent_object = models.Student.objects.filter(**form.cleaned_data).first()

        if not sutdent_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        request.session["info"] = {"id": sutdent_object.id, "username": sutdent_object.account_no, "actor": "student"}
        request.session.set_expiry(60 * 60 * 27)
        return HttpResponse("登陆成功")

    return render(request, 'login.html', {"title": title, "form": form})

def login_teacher(request):

    title = "教师登录"
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"title": title, "form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop("image_code")
        image_code = request.session.get("image_code", "")
        if image_code != user_input_code.upper():
            form.add_error("image_code", "验证码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        teacher_object = models.Teacher.objects.filter(**form.cleaned_data).first()

        if not teacher_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"title": title, "form": form})

        request.session["info"] = {"id": teacher_object.id, "username": teacher_object.account_no, "actor": "teacher"}
        request.session.set_expiry(60 * 60 * 27)
        return HttpResponse("登陆成功")

    return render(request, 'login.html', {"title": title, "form": form})

