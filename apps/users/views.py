from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import BlogUser, EmailVerifyRecord
from utils.send_email import my_send_email

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')

        user = BlogUser()

        user.username = username
        user.password = make_password(password)
        user.email = email
        user.is_active = False
        user.save()
        my_send_email(email)
        return render(request, 'login.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)


        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'error_msg':'用户未激活'})
        else:
            return render(request, 'login.html', {'error_msg': '用户名或者密码错误'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = BlogUser.objects.get(email=email)
                user.is_active = True
                user.save()
                record.delete()

        else:
            return render(request, 'active-fail.html')
        return render(request, 'login.html')
