from rest_framework import serializers
from django.conf import settings
from tickets.models import Ticket, Category

User = settings.AUTH_USER_MODEL


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'ticket_id', 'user', 'content', 'category', 'assign', 'created', 'modified')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
