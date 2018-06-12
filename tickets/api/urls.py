from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from tickets.models import Ticket, Category
from rest_framework import routers

from .views import UserViewSet, TicketViewSet, CategoryViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

router.register(r'tickets', TicketViewSet)

router.register(r'category', CategoryViewSet)

app_name = 'tickets'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]