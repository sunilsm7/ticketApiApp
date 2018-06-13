from rest_framework import serializers
from django.conf import settings # noqa
from tickets.models import Ticket, Category, Comment

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    assign = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'ticket_id', 'user', 'status', 'content', 'assign', 'category', 'created', 'modified')

    def get_user(self, obj):
        return obj.user.username

    def get_assign(self, obj):
        return obj.user.username


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    replies_count = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'ticket',
            'parent',
            'content',
            'updated',
            'timestamp',
            'replies_count'
        ]
        read_only_fields = ('id', 'user', 'timestamp', 'replies_count')

    def get_replies_count(self, obj):
        count = obj.has_replies().count()
        return count

    def get_user(self, obj):
        return obj.user.username
