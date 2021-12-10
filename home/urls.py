from django.urls import path
from home import views as home_views
from django.conf.urls.static import static
from django.conf import settings

# TODO:
# refactor views to home views
urlpatterns = [
    path("", home_views.IndexView.as_view(), name="index"),
    path("home/", home_views.HomeView.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
