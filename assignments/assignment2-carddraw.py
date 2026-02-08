



import requests

# Step 1: Shuffle a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
shuffle_response = requests.get(shuffle_url).json()

deck_id = shuffle_response["deck_id"]

# Step 2: Draw 5 cards using the deck_id
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url).json()

cards = draw_response["cards"]

# Step 3: Print value and suit of each card
print("Your 5 cards are:\n")
for card in cards:
    value = card["value"]
    suit = card["suit"]
    print(f"{value} of {suit}")
