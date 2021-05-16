from django.contrib import admin
from django.urls import path
import newapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', newapp.views.home, name="home"),
    path('blog/<int:blog_id>', newapp.views.detail, name="detail"),
]
