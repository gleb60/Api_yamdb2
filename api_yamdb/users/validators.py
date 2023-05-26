from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(_("Использование имени 'me' запрещено."))

    if not re.match(r'^[\w.@+-]+\z', value):
        raise ValidationError(_(f'{value} содержит недопустимые символы!'))
