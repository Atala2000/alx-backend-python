from rest_framework import serializers
from .models import CustomUser, Message, Conversation

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'user_id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'role',
            'date_joined',
            'last_login',
            'is_active',
            'is_staff',
        ]
        read_only_fields = ['user_id', 'date_joined', 'last_login', 'is_staff']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'message_body', 'sent_at'
        ]


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            'conversation', 'participants'
        ]
