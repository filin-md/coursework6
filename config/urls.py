from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = 'mailing_service'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('mailing.urls', namespace='mailing')),
                  path('', include('users.urls', namespace='users')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
