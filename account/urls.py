from django.conf.urls import url
from account.views import login, signup, logout, test

urlpatterns = [

    url(r'^signup/$', signup, name="signup"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),

    url(r'^test/$', test, name="test"),



]