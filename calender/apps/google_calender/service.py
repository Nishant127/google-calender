from django.conf import settings
import requests
from .exceptions import ACCESS_TOKEN_EXCEPTION, EVENTS_EXCEPTION


class GoogleAuthService:
    @classmethod
    def get_access_token(cls, code):
        try:
            data = {
                "code": code,
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOGGLE_CLIENT_SECRET,
                "redirect_uri": settings.REDIRECT_URI,
                "grant_type": "authorization_code",
            }
            _response = requests.post(settings.TOKEN_URL, data=data)
            return _response.json()["access_token"]
        except:
            raise ACCESS_TOKEN_EXCEPTION(_response.json()["error"])

    @classmethod
    def get_events(cls, access_token):
        try:
            headers = {"Authorization": f"Bearer {access_token}"}
            events_response = requests.get(settings.EVENTS_URL, headers=headers)
            events = events_response.json()["items"]
            return events
        except:
            raise EVENTS_EXCEPTION(events_response.json()["error"]["message"])
