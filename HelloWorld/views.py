from django.shortcuts import render


def runoob(request):
    context = {}
    context["hello"] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, "render.html", context)
