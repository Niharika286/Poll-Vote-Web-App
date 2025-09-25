from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('vote_app/', include('vote_app.urls')),
    path('admin/', admin.site.urls),
]