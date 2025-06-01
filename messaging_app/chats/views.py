from django.shortcuts import render
from .serializers import MessageSerializer, ConversationSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Message, Conversation
from rest_framework.response import Response

# Create your views here.


class MessageViewSet(viewsets.ViewSet):
    """
    Simple Viewset to list messages
    """
    def list(self, request):
        queryset  = Message.objects.all()
        serializer = MessageSerializer(many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset  = Message.objects.all()
        message = get_object_or_404(queryset, pk=pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

class ConversationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Conversation.objects.all()
        serializer = ConversationSerializer(many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.all()
        conversation = get_object_or_404(queryset, pk=pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)