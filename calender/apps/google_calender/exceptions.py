from rest_framework.exceptions import APIException


class ACCESS_TOKEN_EXCEPTION(APIException):
    status_code = 400
    default_detail = "Invalid Code"

    def __init__(self, message):
        self.detail = message


class EVENTS_EXCEPTION(APIException):
    status_code = 400
    default_detail = "Invalid Access Token"

    def __init__(self, message):
        self.detail = message
