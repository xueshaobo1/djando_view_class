# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View,TemplateView
from . import models
class Auth(View):
    def dispatch(self, request, *args, **kwargs):
        username=request.session.get("user_name")
        if not username:
            return redirect("/login/")
        return super(Auth, self).dispatch(request, *args, **kwargs)

class login(TemplateView):

    template_name = 'login.html'
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                user = models.user.objects.get(name = username)
            except:
                return render(request,'login.html')
            if password == user.password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect("/index/")
        return redirect("/login/")

class logout(View):
    def get(self,request):
         if not request.session.get('is_login',None):
             return redirect('/index/')
         request.session.flush()
         return redirect('/index/')

class index(Auth,TemplateView):
    
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['user'] = models.user.objects.all()
        return context





 
