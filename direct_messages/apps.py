from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "direct_messages"
    # admin 패널의 verbose name 수정
    verbose_name = "Direct Messages"
