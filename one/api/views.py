from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
import pytz


@api_view(["GET"])
def get_info(request):
    slack_name = request.query_params.get("slack_name")
    track = request.query_params.get("track")

    github_url = "https://github.com/bensonisaac/one"
    github_file = "https://github.com/bensonisaac/one/blob/main/one/api/views.py"

    current_day = datetime.now().strftime("%A")
    utc_time = datetime.now(pytz.utc)

    if slack_name is None or track is None:
        return Response(
            {"message": "Slack name and track is required"}, status.HTTP_400_BAD_REQUEST
        )
    else:
        return Response(
            {
                "slack_name": slack_name,
                "current_day": current_day,
                "utc_time": utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "track": track,
                "github_file_url": github_file,
                "github_repo_url": github_url,
                "status_code": 200,
            },
            status.HTTP_200_OK,
        )
