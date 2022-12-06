# accounts/urls.py
from django.urls import path

from .views import SignUpView
from .views import dashboard, profile_list, profile

#app_name="accounts2"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]