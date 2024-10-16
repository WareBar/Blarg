from django.urls import path
from . import views

app_name = "POST"

urlpatterns = [
    path("list/", views.post_list, name="list"),
    path("create/", views.post_new, name="new"),
    path("<slug:slug>", views.post_page, name="page")
]
