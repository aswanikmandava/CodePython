from typing import List
from typing import Dict

# typing module allows us to assign a type to the alias

players: List[str] = ["Roger", "Djocovic", "Nadal"]

# create an alias BookPrices
BookPrices = Dict[str, float]

for player in players:
    print(player)

def get_book_stats(bp: BookPrices) -> str:
    num_books = len(bp)
    total_price = sum(bp.values())
    return f"Book Count: {num_books}, Total: {total_price}"

book_prices = {
    "Harry Potter": 19.99,
    "Kingdom": 10.05
}
print(get_book_stats(book_prices))
