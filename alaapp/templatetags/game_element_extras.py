from django import template
from alaapp.utils import System
register = template.Library()

@register.simple_tag
def get_progress_user(ge,user_id):
    return float("%.2f" % ge.get_progress_user(user_id))

