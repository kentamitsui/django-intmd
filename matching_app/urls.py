from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from matching_app.views.index import index
from matching_app.views.login import login_view, logout_view
from matching_app.views.recruitment import recruitment_timeline, recruitment_detail, recruitment_create
from matching_app.views.signup import signup
from matching_app.views.user_profile import user_home, user_profile_detail, user_profile_list, user_profile_update
from matching_app.views.verify import send_new_verification_code, verify_email

urlpatterns = (
    [
        path("signup/", signup, name="signup"),
        path("home/", user_home, name="user_home"),
        path("", index, name="index"),
        path("login/", login_view, name="login"),
        path("logout/", logout_view, name="logout"),
        path("signup/verify/<int:id>/", verify_email, name="verify_email"),
        path("signup/verify/resend/<int:id>/", send_new_verification_code, name="send_new_verification_code"),
        path("profiles/me/update/", user_profile_update, name="user_profile_update"),
        path("profiles/list/", user_profile_list, name="user_profile_list"),
        path("profiles/<int:pk>/", user_profile_detail, name="user_profile_detail"),
        path("recruitments/", recruitment_timeline, name="recruitment_timeline"),
        path("recruitments/<int:pk>/", recruitment_detail, name="recruitment_detail"),
        path("recruitment/create/", recruitment_create, name="recruitment_create"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
