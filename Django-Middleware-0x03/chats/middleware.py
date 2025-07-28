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
    

class OffensiveLanguageMiddleware:

    count = 0

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        self.count += 1
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip_address:
            ip_address = ip_address.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        print(f'Your IP address is: {ip_address}')
        print(f"count is {self.count}")


        return self.get_response(request)
    


class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for chat-related URLs that require admin/moderator access
        if request.path.startswith('/chats/'):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required.")
            
            # Check if user has admin or moderator role
            if not self.has_admin_or_moderator_role(request.user):
                return HttpResponseForbidden("Access denied. Admin or moderator role required.")
        
        response = self.get_response(request)
        return response
    
    def has_admin_or_moderator_role(self, user):
        """Check if user has admin or moderator role"""
        # Check if user is Django superuser (admin)
        if user.is_superuser or user.is_staff:
            return True
        
        # Check if user has admin or moderator role through groups
        user_groups = user.groups.values_list('name', flat=True)
        allowed_roles = ['admin', 'moderator', 'Admin', 'Moderator']
        
        return any(role in user_groups for role in allowed_roles)