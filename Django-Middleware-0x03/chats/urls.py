from django.urls import path, include
from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

# ✅ Step 1: Main router
router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversations')

# ✅ Step 2: Nested router for messages under conversations
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

# ✅ Step 3: Combine all routes
urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
