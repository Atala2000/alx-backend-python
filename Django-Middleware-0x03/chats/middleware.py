from datetime import datetime
import logging


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