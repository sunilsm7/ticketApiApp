from rest_framework import serializers
from django.conf import settings # noqa
from tickets.models import Ticket, Category, Comment

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class TicketSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tickets:tickets-detail', lookup_field='slug')
    user = serializers.SerializerMethodField()
    assign = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'url',
            'slug',
            'title',
            'ticket_id',
            'user',
            'owner',
            'status',
            'content',
            'assign',
            'category',
            'created',
            'modified'
        ]

    def get_user(self, obj):
        return obj.user.username

    def get_assign(self, obj):
        return obj.user.username

    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.user == request.user:
                return True
            return False


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class CommentSerializer(serializers.ModelSerializer):
    replies_count = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='tickets:comment-detail')
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'url',
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
