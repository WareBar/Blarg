from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    path("posts/" , include("POST.urls")),
    path("users/", include("USERS.urls")),

    path('admin/', admin.site.urls),
    path("", views.homePage, name="home"),
    path("about/", views.aboutPage, name="about")
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
