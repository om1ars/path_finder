from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

response = get(BASE_URL + ALL_JSON).json()

def get_links():
    data = get(BASE_URL, ALL_JSON).json()
    links = data['links']

def get_scoreboard():
    scoreboard = 


printer.pprint(scoreBoard)
