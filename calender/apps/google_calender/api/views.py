from rest_framework.views import APIView
from rest_framework import status, response
from django.conf import settings
from django.shortcuts import redirect


class GoogleCalendarInitView(APIView):
    def get(self, request):
        auth_url = f"{settings.AUTH_ENDPOINT}?response_type=code&client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}&scope={settings.SCOPE}"
        return redirect(auth_url)
