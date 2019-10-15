from django.shortcuts import render
# User와 auth 계정에 관한 권한을 다루는 클래스 import
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile

# Create your views here.
def login(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request,\
                                 username= username,\
                                 password= password)
        if user is not None:
            auth.login(request,user)
            return redirect('base',)
        else :
            return render(request, 'loginidx.html', {'error':'username or password is incorrect'})
    else :
        return render(request, 'loginidx.html',)

def signup(request):
    if request.method == "POST" :
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],\
                password=request.POST["password1"]
            )
            nickname = request.POST["nickname"]
            accountnumber = request.POST["Account Number"]
            birthdate = request.POST["Birthdate"]
            phonenumber = request.POST["Phone Number"]
            region = request.POST["Region"]

            profile = Profile(user = user, nickname = nickname,accountnumber=accountnumber,birthdate=birthdate,\
                              phonenumber=phonenumber, region=region, )
            profile.save()

            auth.login(request,user)
            return redirect('base')
        return render(request, 'signupidx.html',)
    return render(request, 'signupidx.html',)

def logout(request):
    # /account/logout href이 있는 버튼을 누르면 로그아웃
    auth.logout(request)
    return redirect('base')

def test(request):
    return render(request, 'loginidx.html',)