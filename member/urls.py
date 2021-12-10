from django.urls import path
from member import views as member_views
from django.conf.urls.static import static
from django.conf import settings

# TODO:
# refactor views to member views
urlpatterns = [
    path("profile/<int:id>/", member_views.UserView.as_view(), name="profile"),
    path(
        "createprofile/",
        member_views.CreateProfileView.as_view(),
        name="createprofile",
    ),
    path(
        "edit_account/<int:id>/",
        member_views.EditProfileView.as_view(),
        name="edit_profile",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
