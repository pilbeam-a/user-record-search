from django import forms
from user_record.models import UserRecord

class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = [
            "first_name",
            "last_name",
            "job_title",
            "phone",
            "email",
        ]
