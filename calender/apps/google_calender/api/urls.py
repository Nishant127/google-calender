from django.urls import path, include
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path("init/", GoogleCalendarInitView.as_view(), name="auth-init"),
    path("redirect/", GoogleCalendarRedirectView.as_view(), name="auth-redirect"),
]
