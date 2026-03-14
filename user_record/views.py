from django.db.models import Q
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_record.models import UserRecord
from user_record.serializers import UserRecordSerializer


@api_view(["GET"])
def api_user_search(request):
    """
    API get endpoint to search user records for the given query q.

    Behaviour:
    -   Only searches once the query is 2 or more characters long.
    -   Searches on first name or last name containing the query.
    """

    q = request.GET.get("q", "").strip()

    # Only filter once 2 or more characters entered in the search
    if len(q) < 2:
        return Response([])

    # Get UserRecords where first or last name contains the query
    results = UserRecord.objects.filter((Q(first_name__icontains=q)) | Q(last_name__icontains=q))

    return Response(UserRecordSerializer(results, many=True).data)


def user_record_home(request):
    """
    Basic view just renders the user_record_home.html
    """

    return render(request, "user_record_home.html")
