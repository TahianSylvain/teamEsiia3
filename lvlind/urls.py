from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include("base.urls")),
    path('api/', include("api.urls")),
    path('account/', include("accounts.urls")),
    path('course/', include("course.urls")),
    path('department/', include("department.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
