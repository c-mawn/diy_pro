from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


import csv
from pathlib import Path
from django.shortcuts import render
from django.conf import settings
import pandas as pd
import logging
from accounts.models import Profile, Tag

from scraping import scraping

logger = logging.getLogger(__name__)


def closest_matches(request):
    csv_path = Path(settings.BASE_DIR) / "resources" / "tools.csv"
    logger.warning(f"CSV path: {csv_path}")

    tools = []
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        tools = df.to_dict(orient="records")
    else:
        logger.warning("CSV file does not exist!")

    breadcrumbs = [
        {"name": "Closest Matches", "url": ""},
    ]

    return render(
        request, "closest_matches.html", {"tools": tools, "breadcrumbs": breadcrumbs}
    )


def purchase_tool(request):
    tool_name = request.GET.get("name", "")

    df = scraping.scrape_tools(tool_name, 10)
    data = df.to_dict(orient="records")

    csv_path = Path(settings.BASE_DIR) / "resources" / "tool_tags.csv"
    if csv_path.exists():
        tags_df = pd.read_csv(csv_path)
        tag_names = tags_df[tags_df["Tool Name"] == tool_name]["Tag"].tolist()
        print(tag_names)
        if tag_names:
            matching_tags = Tag.objects.filter(name__in=tag_names)
            profiles = Profile.objects.filter(tags__in=matching_tags).distinct()
        else:
            profiles = Profile.objects.none()
    else:
        logger.warning("tool_tags.csv does not exist")
        profiles = Profile.objects.none()

    breadcrumbs = [
        {"name": "Closest Matches", "url": "/tools/closest_matches"},
        {"name": tool_name, "url": ""},
    ]

    return render(
        request,
        "purchase_tools.html",
        {
            "tools": data,
            "tool_name": tool_name,
            "breadcrumbs": breadcrumbs,
            "profiles": profiles,
        },
    )
