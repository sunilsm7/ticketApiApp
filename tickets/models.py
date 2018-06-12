import uuid
from django.conf import settings
from django.db import models
# Create your models here.

from django.contrib.auth.models import User


def generate_ticket_id():
    # generate unique ticket id
    return str(uuid.uuid4()).split("-")[-1]


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    status = (
        ("Open", "open"),
        ("PROGRESS", "progress"),
        ("PENDING", "pending"),
        ("HOLD", "hold"),
        ("REOPEN", "reopen"),
        ("RESOLVED", "resolved"),
        ("CLOSED", "closed"),
    )

    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_created')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ticket_category')
    ticket_id = models.CharField(max_length=255, blank=True)
    assign = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='ticket_assign')
    status = models.CharField(choices=status, max_length=155, default="pending")
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Ticket'
        ordering = ["-created"]

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs)
