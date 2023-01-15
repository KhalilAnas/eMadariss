from trello.trelloclient import TrelloClient

api_key = "your_api_key_trello"
api_token = "your_trello_token"

client = TrelloClient(api_key=api_key, token=api_token)

class Trello:
    def check_cards(list_id="your_list_id"):
        list_to_check = client.get_list(list_id)
        cards_names = [card_name.name for card_name in list_to_check.list_cards()]  
        return cards_names

    def send_card(name, desc, list_id="your_list_id"):
        list_to_send_to = client.get_list(list_id)
        list_to_send_to.add_card(name, desc)
