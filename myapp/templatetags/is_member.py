from django import template
register = template.Library()

@register.filter
def is_member(list_of_responses, id):
    for item in list_of_responses:
        if id == item.question_id:
            return "yes"
    return "no"
