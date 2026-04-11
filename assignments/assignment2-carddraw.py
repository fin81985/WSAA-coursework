# assignment 1
# Author : Finian Doonan



import requests

# Step 1: Shuffle a new deck
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"  # URL to shuffle a new deck of cards
response = requests.get(shuffle_url).json() # Send request to shuffle the deck and get the response as json
deck_id = response["deck_id"]

# Step 2: Draw 5 cards using the deck_id
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"  # URL to draw 5 cards from the deck we just shuffled
draw_response = requests.get(draw_url).json()

cards = draw_response["cards"]

# Step 3: Print value and suit of each card
print("Your 5 cards are:\n")
for card in cards:
    value = card["value"]
    suit = card["suit"]
    print(f"{value} of {suit}")
