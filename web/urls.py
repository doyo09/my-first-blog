from django.conf.urls import url
from django.contrib import admin
from web.views import about, index, howtouse, howtouse_video, refund

urlpatterns = [

    url(r'^$', index, name="base"),
    url(r'^about/$', about, name="about"),
    url(r'^howtouse/$', howtouse, name="howtouse"),
    url(r'^howtousewithVideo/$', howtouse_video, name="howtouseVideo"),
    url(r'^refund/$', refund, name="refund"),

]