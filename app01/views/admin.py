# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from app01 import models
from app01.utils.form import AdminAdd,StudentAdd,TeacherAdd,AdminEdit,StudentEdit,TeacherEdit,AdminReset,StudentReset,TeacherReset
from app01.utils.pagination import PagInation


def admin_home(request):

    return render(request, "admin_layout.html")


def list_admin(request):

    #搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["moblie__contains"] = search_data

    queryset = models.Admin.objects.filter(**data_dict)

    page_object = PagInation(request, queryset)

    context = {
        "queryset" : page_object.page_queryset,
        "page_string" : page_object.html(),
        "search_data" : search_data
    }

    return render(request, 'admin_list.html', context)

def add_admin(request):

    title = "新建管理员"
    if request.method == "GET":
        form = AdminAdd()
        return render(request, "change.html", {"form": form, "title": title})

    form = AdminAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/list/admin/')

    return render(request, "change.html", {"form": form, "title": title})

def edit_admin(request, nid):

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/admin/")

    title = "修改管理员信息"
    if request.method == "GET":
        form = AdminEdit(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})

    form = AdminEdit(data=request.POST,  instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/list/admin/')

    return render(request, "change.html", {"form": form, "title": title})

def delete_admin(request, nid):

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/admin/")

    models.Admin.objects.filter(id=nid).delete()

    return redirect('/list/admin/')

def reset_admin(request, nid):

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/admin/")

    title = "重置密码-{}".format(row_object.account_no)

    if request.method == "GET":
        form = AdminReset()
        return render(request, "change.html", {"form": form, "title": title})

    form = AdminReset(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/list/admin/")

    return render(request, "change.html", {"form": form, "title": title})

def list_student(request):

    #搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["moblie__contains"] = search_data

    queryset = models.Student.objects.filter(**data_dict)

    page_object = PagInation(request, queryset)

    context = {
        "queryset" : page_object.page_queryset,
        "page_string" : page_object.html(),
        "search_data" : search_data
    }

    return render(request, 'student_list.html', context)

def add_student(request):

    title = "新建学生"
    if request.method == "GET":
        form = StudentAdd()
        return render(request, "change.html", {"form": form, "title": title})

    form = StudentAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/list/student/')

    return render(request, "change.html", {"form": form, "title": title})

def edit_student(request, nid):

    row_object = models.Student.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/student/")

    title = "修改学生信息"
    if request.method == "GET":
        form = StudentEdit(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})

    form = StudentAdd(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/list/student/')

    return render(request, "change.html", {"form": form, "title": title})

def delete_student(request, nid):

    row_object = models.Student.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/student/")

    models.Student.objects.filter(id=nid).delete()

    return redirect('/list/student/')

def search_student(request):
    if request.method == "GET":
        return render(request, "student_query.html")
    else:
        no = request.POST.get("number")
        # no = eval(string)
        # no = int(no)
        # student = models.Student.objects.filter(stu_no=stu_no, role=1).first()
        student = models.Student.objects.filter(stu_no=no).first()

        return render(request, "student_query.html", {
            "stu_no": student.stu_no if student else "查询无此学生",
            "name": student.name if student else "查询无此学生",
            "grade": student.grade if student else "查询无此学生",
            "major": student.major if student else "查询无此学生",
            "Class": student.Class if student else "查询无此学生",
            "phone_no": student.phone_no if student else "查询无此学生",
        })

# def search_student(request, acc_no):
#
#     row_object = models.Student.objects.filter(account_no=acc_no).first()
#     if not row_object:
#         return redirect("/list/student/")
#
#     models.Student.objects.filter(account_no=acc_no).delete()
#
#     models.Student.objects.filter(account_no=acc_no)
#
#     return redirect('/list/student/')

# def search_student(request):
#     q = request.GET.get('q')
#     error_msg = ''
#
#     if not q:
#         error_msg = '请输入关键词'
#         return render(request, 'errors.html', {'error_msg': error_msg})
#
#     student_list = models.Student.objects.filter(title__icontains=q)
#     return render(request, 'blog/results.html', {'error_msg': error_msg,
#                                                'student_list': student_list})

    # row_object = models.Student.objects.filter(account_no=acc_no).first()
    # if not row_object:
    #     return redirect("/list/student/")
    #
    # models.Student.objects.filter(account_no=acc_no).delete()
    #
    # models.Student.objects.filter(account_no=acc_no)

def reset_student(request, nid):

    row_object = models.Student.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/student/")

    title = "重置密码-{}".format(row_object.account_no)

    if request.method == "GET":
        form = StudentReset()
        return render(request, "change.html", {"form": form, "title": title})

    form = StudentReset(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/list/student/")

    return render(request, "change.html", {"form": form, "title": title})

def list_teacher(request):
    #搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["moblie__contains"] = search_data

    queryset = models.Teacher.objects.filter(**data_dict)

    page_object = PagInation(request, queryset)

    context = {
        "queryset" : page_object.page_queryset,
        "page_string" : page_object.html(),
        "search_data" : search_data
    }

    return render(request, 'teacher_list.html', context)

def add_teacher(request):

    title = "新建教师"
    if request.method == "GET":
        form = TeacherAdd()
        return render(request, "change.html", {"form": form, "title": title})

    form = TeacherAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/list/teacher/')

    return render(request, "change.html", {"form": form, "title": title})

def edit_teacher(request, nid):

    row_object = models.Teacher.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/teacher/")

    title = "修改教师信息"
    if request.method == "GET":
        form = TeacherEdit(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})

    form = TeacherEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/list/teacher/')

    return render(request, "change.html", {"form": form, "title": title})

def delete_teacher(request, nid):

    row_object = models.Teacher.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/teacher/")

    models.Teacher.objects.filter(id=nid).delete()

    return redirect('/list/teacher/')

def reset_teacher(request, nid):

    row_object = models.Teacher.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/list/teacher/")

    title = "重置密码-{}".format(row_object.account_no)

    if request.method == "GET":
        form = TeacherReset()
        return render(request, "change.html", {"form": form, "title": title})

    form = TeacherReset(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/list/teacher/")

    return render(request, "change.html", {"form": form, "title": title})
