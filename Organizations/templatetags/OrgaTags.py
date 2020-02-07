from django import template
from django.contrib import messages
from django.contrib.messages.storage.base import Message


register = template.Library()


msg_level_to_Bootstrap = {
    messages.DEBUG:   ("primary", "white"),
    messages.INFO:    ("info",    "white"),
    messages.SUCCESS: ("success", "white"),
    messages.WARNING: ("warning", "dark"),
    messages.ERROR:   ("danger",  "white"),
}


@register.filter
def get_Bootstrap_class(msg, arg="contextual"):
    if not isinstance(msg, Message):
        return ""

    if msg.level not in msg_level_to_Bootstrap:
        return ""

    if arg == "contextual":
        return msg_level_to_Bootstrap[msg.level][0]

    if arg == "white-dark":
        return msg_level_to_Bootstrap[msg.level][1]

    return ""
