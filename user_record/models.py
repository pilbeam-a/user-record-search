from django.db import models

from user_record.validators import uk_mobile_phone_validator

class BaseModel(models.Model):
    """
    Base model.

    - created_at: record datetime of object creation
    - updated_at: record datetime of last object update
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserRecord(BaseModel):
    """
    Model to store User records.

    Behaviour:
    -   Full name (First name and Last name) must be unique
    -   Phone and Email must be unique
    -   Phone must be a valid UK mobile phone number (uses uk_mobile_phone_validator)
    -   Email must be a valid email address
    """

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, unique=True, validators=[uk_mobile_phone_validator,])
    email = models.EmailField(max_length=250, unique=True)

    class Meta:
        unique_together = ["first_name", "last_name"]
