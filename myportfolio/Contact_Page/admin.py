from django.conf import settings
from django.contrib import admin
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactMessage, MapSide


@admin.register(MapSide)
class MapSideAdmin(admin.ModelAdmin):
    list_display = ('Address', 'PhoneNumber', 'Email')
    search_fields = ('Address', 'PhoneNumber', 'Email')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'has_reply', 'created_at', 'replied_at')
    search_fields = ('name', 'email', 'subject', 'message', 'reply')
    list_filter = ('created_at', 'replied_at')
    date_hierarchy = 'created_at'

    def has_reply(self, obj):
        return bool(obj.reply)
    has_reply.boolean = True
    has_reply.short_description = 'Replied'


@receiver(post_save, sender=ContactMessage)
def send_reply_email(sender, instance, **kwargs):
    if instance.reply:
        send_mail(
            subject=f"Reply: {instance.subject}",
            message=instance.reply,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
