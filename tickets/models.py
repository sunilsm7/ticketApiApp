import uuid
from django.conf import settings
from django.db import models
# Create your models here.

# from django.contrib.auth.models import User


def generate_ticket_id():
    # generate unique ticket id
    return str(uuid.uuid4()).split("-")[-1]


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = '01 Category'

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ticket_created')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ticket_category')
    ticket_id = models.CharField(max_length=255, blank=True)
    assign = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='ticket_assign')
    status = models.CharField(choices=status, max_length=155, default="pending")
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '02 Ticket'
        ordering = ["-created"]

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs)

    @property
    def get_comments(self):
        qs = self.comments.all()
        return qs


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '03 Comments'
        ordering = ['-timestamp']

    def __str__(self):
        return '{} {}'.format(self.user, self.content, self.parent)

    def has_replies(self):
        return Comment.objects.filter(parent=self)
