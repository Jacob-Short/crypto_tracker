from django.urls import path
from messaging import views as messaging_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(
        "message/<int:id>",
        messaging_views.SendMessageView.as_view(),
        name="send-message",
    ),
    path("my-messages/<int:id>/", messaging_views.member_messages, name="my-messages"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
