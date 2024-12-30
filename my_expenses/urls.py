from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = ([
    path("",views.my_expenses,name="my_expenses"),
    path("upload", views.upload_csv, name='upload_csv'),
    path("downloadSample", views.download_sample, name='download_sample'),
])
               # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))