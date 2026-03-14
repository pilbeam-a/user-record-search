from django.db import models

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
    - first_name and last_name must be unique together
    - phone and email must be unique
    """

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)

    class Meta:
        unique_together = ["first_name", "last_name"]
