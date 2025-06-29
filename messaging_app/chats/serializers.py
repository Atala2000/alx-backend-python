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
    sender = CustomUserSerializer(read_only=True)
    message_body = serializers.CharField(max_length=1000)  # ✅ Added CharField

    class Meta:
        model = Message
        fields = [
            'id',
            'message_body',
            'sent_at',
            'sender',
        ]

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")  # ✅ ValidationError
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = [
            'conversation_id',
            'participants',
            'messages',
        ]

    def get_messages(self, obj):
        messages = obj.message_set.all().order_by('sent_at')
        return MessageSerializer(messages, many=True).data
