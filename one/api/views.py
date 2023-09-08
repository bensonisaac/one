from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.utils import timezone
import json


@api_view(["GET"])
def get_info(request):
    slack_name = request.query_params.get("slack_name")
    track = request.query_params.get("track")

    github_url = "https://github.com/bensonisaac/one"
    github_file = "https://github.com/bensonisaac/one/blob/main/one/manage.py"

    current_day = datetime.now().strftime("%A")
    utc_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S %Z")

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file,
        "github_repo_url": github_url,
        "status_code": 200,
    }
    format = json.dumps(data, indent=4)

    format_data = json.loads(format)

    if slack_name is None or track is None:
        return Response(
            {"message": "Slack name and track is required"}, status.HTTP_400_BAD_REQUEST
        )
    else:
        return Response(
            format_data,
            status.HTTP_200_OK,
        )
