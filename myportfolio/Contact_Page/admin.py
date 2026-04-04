from django.contrib import admin
from django.conf import settings
from .models import ContactMessage
from .models import MapSide
# Register your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class MapSide_Admin(admin.ModelAdmin):
    list_display = ('Address','PhoneNumber','Email')
# admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(MapSide,MapSide_Admin)


@receiver(post_save, sender=ContactMessage)
def send_reply_email(sender, instance, **kwargs):
    if instance.reply:  # agar reply likha gaya hai
        send_mail(
            subject=f"Reply: {instance.subject}",
            message=instance.reply,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )

class Admin_msg(admin.ModelAdmin):
    list_display = ('name','email','subject')

admin.site.register(ContactMessage,Admin_msg)
