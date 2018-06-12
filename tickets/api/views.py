from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer, TicketSerializer, CategorySerializer
from tickets.models import Ticket, Category
from django.contrib.auth.models import User
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
