from rest_framework.exceptions import APIException


class ACCESS_TOKEN_EXCEPTION(APIException):
    status_code = 400
    default_detail = "Invalid code"

    def __init__(self, message):
        self.detail = message