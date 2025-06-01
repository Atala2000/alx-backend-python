from django.urls import path
from .views import ConversationViewSet, MessageViewSet
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

router = DefaultRouter()

router.register('messages', MessageViewSet, basename='messages')
router.register('converstions', ConversationViewSet, basename='conversations')

urlpatterns = [
    # path('test', )
]

urlpatterns += router.urls