from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('MyNewTab.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls'))
]
