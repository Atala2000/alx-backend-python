from datetime import datetime
import logging
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied



class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
            filename="requests.log",
            level=logging.INFO
        )

    def __call__(self, request):
        
        user = request.user
        print(f"{datetime.now()} - User: {user} - Path: {request.path}")

        logging.info(
            f"{datetime.now()} - User: {user} - Path: {request.path}"
        )

        response = self.get_response(request)




        return response
    

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now()
        print(now)

        # Define allowed access window
        dt1 = datetime(now.year, now.month, now.day, 9, 0)   # 9:00 AM
        dt2 = datetime(now.year, now.month, now.day, 18, 0)  # 6:00 PM

        # Deny access if outside allowed time
        if not (dt1 <= now <= dt2):
            raise PermissionDenied("Access is only allowed between 9 AM and 6 PM.")


        return self.get_response(request)