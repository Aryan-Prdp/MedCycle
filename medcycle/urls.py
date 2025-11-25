from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('auth/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', core_views.register, name='register'),

    # Core App URLs
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
