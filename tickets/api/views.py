from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket, Category, Comment
from .serializers import UserSerializer, TicketSerializer, CategorySerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)
