__author__ = 'dart_vaider'
from django import template
import datetime
register = template.Library()

# @register.filter(name = 'cut')
def cut(value, arg):
    return value.replace(arg, "")
# @register.filter
def lower(value):
    return value.lower()

register.filter('cut', cut)
register.filter('lower', lower)

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)

# @register.tag(name = 'current_time')
def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return CurrentTimeNode(format_string[1:-1])

register.tag('current_time', do_current_time)