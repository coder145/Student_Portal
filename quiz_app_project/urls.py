from django.urls import path, re_path

from . import views

urlpatterns = [
    path("",views.index,name = "index"),
    re_path("([0-9]{9})/$",views.main_page, name = "main_page"),
    path("sign_up/",views.sign_up, name = "sign_up")
]