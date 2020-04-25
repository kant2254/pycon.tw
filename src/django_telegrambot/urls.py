
from django.conf.urls import url
from . import views
from django.conf import settings
from . import telegramBotSettings

webhook_base = telegramBotSettings.DJANGO_TELEGRAMBOT.get('WEBHOOK_PREFIX','/')
if webhook_base.startswith("/"):
    webhook_base = webhook_base[1:]
if not webhook_base.endswith("/"):
    webhook_base += "/"

urlpatterns = [
    url(r'{}(?P<bot_token>.+?)/$'.format(webhook_base), views.webhook, name='webhook'),
]