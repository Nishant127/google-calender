from rest_framework.views import APIView
from rest_framework import status, response
from django.conf import settings
from django.shortcuts import redirect
import requests
from google_calender.service import GoogleAuthService


class GoogleCalendarInitView(APIView):
    def get(self, request):
        auth_url = f"{settings.AUTH_URL}?response_type=code&client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}&scope={settings.SCOPE}"
        return redirect(auth_url)


class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        code = request.query_params["code"]
        access_token = GoogleAuthService.get_access_token(code)
        events = GoogleAuthService.get_events(access_token)
        return response.Response(data={"Events": events})
