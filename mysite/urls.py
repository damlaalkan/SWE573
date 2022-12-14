
from django.contrib import admin
from django.urls import path, include # new
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path("", include("accounts.urls")), #new
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    path("accounts/", include("accounts.urls")),
    
]
