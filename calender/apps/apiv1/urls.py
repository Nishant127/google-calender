from django.urls import path, include

urlpatterns = [
    path("calender/", include("google_calender.api.urls"), name="calender_api"),
]
