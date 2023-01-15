from trello.trelloclient import TrelloClient

api_key = "d3256ebc6e002a342b9731ae45f24c84"
api_token = "ATTA4775160d7a0ffdc047659a3fbdd1aca131c6b882dc564a256a3daf00397d9008723FB6F5"

client = TrelloClient(api_key=api_key, token=api_token)

class Trello:
    def check_cards(list_id="63a1eab5d2ce2a0316d53c4e"):
        list_to_check = client.get_list(list_id)
        cards_names = [card_name.name for card_name in list_to_check.list_cards()]  
        return cards_names

    def send_card(name, desc, list_id="63a1eab5d2ce2a0316d53c4e"):
        list_to_send_to = client.get_list(list_id)
        list_to_send_to.add_card(name, desc)