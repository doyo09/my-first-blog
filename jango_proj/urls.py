"""jango_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from web.views import main, about, index
from blog.views import post_list1, post_detail, post_new, post_edit

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # "blog" APP의 url등록
    url(r'^blog/', include('blog.urls')),
    # url(r'^blog/$', post_list, name="blog"), 버린거니까 무시
    # 위, 아래 둘중 하나
    # url(r'^blog/$', post_list1, name="blog"),
    #
    # url(r'^blog/post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    # url(r'^blog/post/new/$', post_new, name='post_new'),
    # url(r'^blog/post/(?P<pk>[0-9]+)/edit', post_edit, name='post_edit'),

    # "web" APP의 main
    url(r'^$', main, name="home"),

    # "web" APP의 url등록
    url(r'^base/', include('web.urls')),
    # url(r'^base/$', index, name="base"),
    # url(r'^base/about/$', about, name="about"),

    # "account" APP의 url등록
    url(r'^account/', include('account.urls')),


]
