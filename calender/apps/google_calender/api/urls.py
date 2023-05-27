from django.urls import path, include
from .views import GoogleCalendarInitView, GoogleCaledarRedirectView

urlpatterns = [
    path("init/", GoogleCalendarInitView.as_view(), name="auth-init"),
    path("redirect/", GoogleCaledarRedirectView.as_view(), name="auth-redirect"),
]
