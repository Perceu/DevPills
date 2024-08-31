# continuando nossa serie sobre requests
# agora falaremos sobre a parsel lib que 
# ajuda muito na raspagem de dados interpretando o html e 
# transformando num objeto mais facil de navegar

import requests
import pprint
from parsel import Selector

base_url = "https://www.gamespot.com/articles/"
article_url = "2024-upcoming-games-release-schedule/1100-6518504/"
full_url = f"{base_url}{article_url}"

response = requests.get(
    full_url
)

html_selector = Selector(text=response.text)
games = html_selector.xpath(
    '//p[contains(@dir,"ltr")]/text()').getall()

pprint.pprint(
    games,
    indent=4
)