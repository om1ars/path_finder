from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

response = get(BASE_URL + ALL_JSON).json()

links = response['links']

scoreBoard = links['currentScoreBoard']

printer.pprint(scoreBoard)