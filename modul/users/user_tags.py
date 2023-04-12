from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def get_user_groups(user):
    groups = user.groups.all()
    return [group.name for group in groups]