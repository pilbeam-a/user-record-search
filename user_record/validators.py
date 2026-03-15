from django.core.validators import RegexValidator

uk_mobile_phone_validator = RegexValidator(
    regex=r'^(\+44|0)7\d{9}$',
    message="Enter a valid UK mobile phone number."
)
