from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


import csv
from pathlib import Path
from django.shortcuts import render
from django.conf import settings
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def closest_matches(request):
    csv_path = Path(settings.BASE_DIR) / "resources" / "tools.csv"
    logger.warning(f"CSV path: {csv_path}")

    tools = []
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        logger.warning(f"CSV DataFrame:\n{df}")
        tools = df.to_dict(orient="records")
    else:
        logger.warning("CSV file does not exist!")

    return render(request, "closest_matches.html", {"tools": tools})
