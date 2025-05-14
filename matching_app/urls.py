from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ルートURLに対するビューを設定
]