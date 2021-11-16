from django.urls import path
from api import views as api_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('my-ct/', api_views.Dashboard.as_view(), name='dashboard'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)