from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path("analysis/",views.analysis, name="analysis"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
