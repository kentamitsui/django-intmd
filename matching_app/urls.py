from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from matching_app.views.signup import signup
from matching_app.views.user_profile import user_home
from matching_app.views.index import index
from matching_app.views.login import login_view, logout_view

urlpatterns = (
    [
        path("signup/", signup, name="signup"),
        path("home/", user_home, name="user_home"),
        path("", index, name="index"),
        path("login/", login_view, name="login"),
        path("logout/", logout_view, name="logout")
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
