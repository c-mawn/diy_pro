import requests
import urllib.parse
from bs4 import BeautifulSoup
import os
import time
import pandas as pd

TOKEN = os.environ.get("TOKEN")


def scrape_tools(input_tool_name, num_results):
    start_time = time.time()
    tool_name = input_tool_name.replace(" ", "+")
    current_url = "https://www.ebay.com/sch/i.html?_nkw=" + tool_name

    encoded_url = urllib.parse.quote_plus(current_url)
    api_url = f"https://api.scrape.do/?token={TOKEN}&url={encoded_url}&geocode=us&super=true&render=false"

    response = requests.get(api_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # first two results are irrelevant
    cards = soup.select("div.su-card-container.su-card-container--horizontal")[
        2 : 2 + num_results
    ]
    print(f"Found {len(cards)} cards.")

    data = []

    for card in cards:
        try:
            tool_name = card.select_one(
                "div.s-card__title span.su-styled-text"
            ).get_text(strip=True)
        except AttributeError:
            tool_name = None

        try:
            price = card.select_one(".s-card__price").get_text(strip=True)
        except AttributeError:
            price = None

        try:
            image_url = card.select_one(".s-card__image")["src"]
        except (AttributeError, TypeError):
            image_url = None

        try:
            raw_link = card.select_one("a.s-card__link")["href"]
            listing_link = raw_link.split("?")[0]
        except (AttributeError, TypeError):
            listing_link = None

        data.append(
            {
                "tool_name": tool_name,
                "price": price,
                "image_url": image_url,
                "listing_link": listing_link,
            }
        )

    df = pd.DataFrame(data)

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    print("Scraping completed. Returning DataFrame.")

    return df
