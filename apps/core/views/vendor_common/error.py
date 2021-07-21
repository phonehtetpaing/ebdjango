# -*- Coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def view_500(request):
    #TODO make this work
    return render(request, "common/500.html")


def view_404(request, exception):

    return redirect('/')


def view_403(request, exception):

    return redirect('/')
