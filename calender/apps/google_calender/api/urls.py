from django.urls import path, include
from .views import GoogleCalendarInitView

urlpatterns = [path("init/", GoogleCalendarInitView.as_view(), name="calender-init")]
