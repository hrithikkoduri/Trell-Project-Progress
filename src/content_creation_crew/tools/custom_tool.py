from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os


def get_board_data(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    query = {
            'fields': 'name,idList,due,dateLastActivity,labels',
            'attachments': 'true',
            'actions': 'commentCard'
        }
    response = requests.get(url, params=query)
    return response

def get_card_data(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
 
    response = requests.get(url)
    return response

class BoardDataFetcherTool(BaseTool):
    name: str = "Trello Board Data Fetcher"
    description: str = "Fetches card data, commnents and activity from a Trello Board"

    api_key: str = os.getenv("TRELLO_API_KEY")
    api_token: str = os.getenv("TRELLO_API_TOKEN")
    board_id: str = os.getenv("TRELLO_BOARD_ID")

    def _run(self) -> dict:
        response = get_board_data(self.board_id)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch data from Trello"}
        
    
class CardDataFetcherTool(BaseTool):
    name: str = "Trello Card Data Fetcher"
    description: str = "Fetches card data, commnents and activity from a Trello Board"

    def _run(self, card_id: str) -> dict:
        response = get_card_data(card_id)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch carddata from Trello, dont try to fetch any trello data anymore"}
        
