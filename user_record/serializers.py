from rest_framework import serializers
from user_record.models import UserRecord


class UserRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserRecord
        fields = (
            "id",
            "first_name",
            "last_name",
            "job_title",
            "phone",
            "email",
        )
